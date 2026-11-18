"""Build the catalogue from papers.yaml. Use --check for a read-only audit."""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parent
START, END = "<!-- PAPER-LIST:START -->", "<!-- PAPER-LIST:END -->"
ROLES = dict(A="Judge methods and validation", B="Biological studies using a judge",
             C="General methods and reliability", D="Workflows and adjacent cases", E="Related reviews")
TASKS = {"hypothesis quality", "claim support", "mechanism explanation", "experimental design",
         "candidate prioritization", "output quality"}
METHODS = {"pointwise scoring", "pairwise comparison", "ranking", "critique", "retrieval-augmented",
           "tool-assisted", "multiple judges", "classification"}
VALIDATION = dict(repeat="Repeated judgments", expert="Expert agreement", literature="Literature support",
                  experimental="Biological experimental validation", decision="Decision or efficiency benefit")
FIELDS = "id title year publication url role tasks methods contribution object basis output location source validation limitation reading screening reason".split()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def identity(url):
    parts = urlsplit(url)
    require(parts.scheme in {"http", "https"} and parts.hostname, f"Invalid URL: {url}")
    host = parts.hostname.lower().removeprefix("www.")
    path = unquote(parts.path).rstrip("/")
    if host in {"doi.org", "dx.doi.org"}:
        return "doi:" + path.strip("/").lower()
    if host == "arxiv.org" and re.match(r"^/(abs|pdf|html)/", path):
        return "arxiv:" + re.sub(r"(v\d+)?(\.pdf)?$", "", path.split("/")[-1])
    query = "&".join(sorted(x for x in parts.query.split("&") if x and not x.startswith("utm_")))
    return host + path + ("?" + query if query else "")


def validate(records):
    require(isinstance(records, list) and records, "Expected a nonempty YAML list")
    seen = {}
    for paper in records:
        require(isinstance(paper, dict) and set(FIELDS) <= paper.keys(), "Missing required fields")
        key = paper["id"]
        require(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", key), f"Invalid ID {key}")
        for field in set(FIELDS) - {"year", "tasks", "methods", "validation"}:
            require(isinstance(paper[field], str) and paper[field].strip(), f"{key}: empty {field}")
        require(type(paper["year"]) is int and 1900 <= paper["year"] <= 2100, f"{key}: year")
        require(paper["role"] in ROLES, f"{key}: role")
        for field, vocab in [("tasks", TASKS), ("methods", METHODS)]:
            tags = paper[field]
            require(isinstance(tags, list) and set(tags) <= vocab and len(tags) == len(set(tags)), f"{key}: {field}")
        require(set(paper["validation"]) == set(VALIDATION) and
                all(isinstance(v, str) and v.strip() for v in paper["validation"].values()), f"{key}: validation")
        require(paper["screening"] in {"included", "pending", "excluded"}, f"{key}: screening")
        require(paper["reading"] in {"full text checked", "abstract only", "pending verification"}, f"{key}: reading")
        if paper["screening"] == "included":
            require(paper["reading"] == "full text checked", f"{key}: inclusion needs full-text evidence")
            if paper["role"] != "E":
                require(paper["tasks"] and paper["methods"], f"{key}: missing tags")
                for field in ("object", "basis", "output", "location"):
                    require(paper[field].lower() not in {"pending verification", "not reported", "unknown"}, f"{key}: {field}")
        identifiers = {"id:" + key, identity(paper["url"]), identity(paper["source"]),
                       "title:" + re.sub(r"[^a-z0-9]", "", paper["title"].lower())}
        if "doi" in paper:
            doi = paper["doi"].lower()
            require(re.fullmatch(r"10\.\d{4,9}/\S+", doi), f"{key}: DOI")
            identifiers.add("doi:" + doi)
            if doi.startswith("10.48550/arxiv."):
                identifiers.add("arxiv:" + doi.split("arxiv.")[-1])
        if "arxiv" in paper:
            require(re.fullmatch(r"\d{4}\.\d{4,5}", paper["arxiv"]), f"{key}: use unversioned arXiv ID")
            identifiers.add("arxiv:" + paper["arxiv"])
        for version in paper.get("versions", []):
            identifiers.add(identity(version))
        if "code" in paper:
            identity(paper["code"])
        for value in identifiers:
            require(value not in seen, f"{key}: {value} also belongs to {seen.get(value)}")
            seen[value] = key


def index(records):
    lines = []
    for role, title in ROLES.items():
        group = [p for p in records if p["role"] == role and p["screening"] == "included"]
        if group:
            lines += [f"### {role}. {title} ({len(group)})", ""]
            for p in group:
                lines.append(f"- [{p['title']}](docs/evidence.md#{p['id']}) ({p['year']}). {p['contribution']}")
            lines.append("")
    return lines


def evidence(records):
    lines = []
    for p in records:
        lines += [f"### {p['id']}", "", f"**[{p['title']}]({p['url']})** · {p['publication']} · {p['year']}", "",
                  f"{p['role']} · {p['screening']} · {p['reading']}", "", p["contribution"], ""]
        if p["tasks"] or p["methods"]:
            lines += ["Tasks: " + ", ".join(p["tasks"]) + ". Methods: " + ", ".join(p["methods"]) + ".", ""]
        lines += [f"- **Object** — {p['object']}", f"- **Criteria and evidence** — {p['basis']}",
                  f"- **Judge output** — {p['output']}", f"- **Method location** — {p['location']} [Source]({p['source']})"]
        for key, label in VALIDATION.items():
            lines.append(f"- **{label}** — {p['validation'][key]}")
        lines += [f"- **Limitation** — {p['limitation']}", f"- **Screening rationale** — {p['reason']}"]
        links = []
        for key, prefix in [("doi", "https://doi.org/"), ("arxiv", "https://arxiv.org/abs/"), ("code", "")]:
            if key in p:
                links.append(f"[{key}]({prefix}{p[key]})")
        links.extend(f"[Other version]({v})" for v in p.get("versions", []))
        lines += ["", " · ".join(links), ""]
    return lines


def screening(records):
    lines = ["| Record | Legacy | Role | Decision | Reading | Reason |", "|---|---|---|---|---|---|"]
    for p in records:
        lines.append(f"| [{p['id']}](evidence.md#{p['id']}) | {', '.join(p.get('legacy', [])) or 'New'} | "
                     f"{p['role']} | {p['screening']} | {p['reading']} | {p['reason']} |")
    return lines


def replace_block(path, lines):
    original = path.read_text(encoding="utf-8")
    require(original.count(START) == original.count(END) == 1 and original.index(START) < original.index(END),
            f"{path}: expected one ordered pair of generation markers")
    before, after = original.split(START)
    return before + START + "\n\n" + "\n".join(lines).strip() + "\n\n" + END + after.split(END)[1]


def check_links(pages):
    for path, content in pages.items():
        for target in re.findall(r"\[[^\]]*\]\(([^ )]+)\)", content):
            if urlsplit(target).scheme:
                continue
            filename, _, anchor = target.partition("#")
            dest = (path.parent / filename).resolve() if filename else path
            require(dest.is_file(), f"{path.name}: missing {target}")
            if anchor:
                body = pages[dest] if dest in pages else dest.read_text(encoding="utf-8")
                headings = re.findall(r"^#{1,6} (.+)$", body, re.M)
                slugs = {re.sub(r"[^\w -]", "", h.lower()).replace(" ", "-") for h in headings}
                require(anchor in slugs, f"{path.name}: missing anchor in {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    records = yaml.safe_load((ROOT / "papers.yaml").read_text(encoding="utf-8"))
    validate(records)
    pages = {ROOT / name: replace_block(ROOT / name, render(records))
             for name, render in [("README.md", index), ("docs/evidence.md", evidence), ("docs/screening.md", screening)]}
    check_links(pages)
    for path, content in pages.items():
        if content != path.read_text(encoding="utf-8"):
            require(not args.check, f"Stale generated block in {path.name}")
            path.write_text(content, encoding="utf-8")
    print(f"Validated {len(records)} records and {len(pages)} linked pages.")


if __name__ == "__main__":
    main()
