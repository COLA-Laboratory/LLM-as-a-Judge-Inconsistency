"""Build the catalogue from papers.yaml. Use --check for a read-only audit."""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

from assets.validation_map import evidence_map

ROOT = Path(__file__).resolve().parent
BRANCHES = ("claim support", "hypothesis qualities", "research outputs")
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
        require(set(paper["validation"]) == set(VALIDATION), f"{key}: missing validation endpoint")
        core = paper["role"] in {"A", "B"} and paper["screening"] == "included"
        if core:
            home = paper.get("homepage", {})
            require(home.get("branch") in BRANCHES, f"{key}: unknown homepage branch")
            require(all(isinstance(home.get(k), str) and home[k].strip() for k in
                        ("name", "venue", "task", "method", "validation")), f"{key}: comparison fields")
        for field, item in paper["validation"].items():
            if isinstance(item, dict):
                require(item.get("status") == "reported" and all(isinstance(item.get(k), str) and
                        item[k].strip() for k in ("label", "detail")), f"{key}: invalid {field} evidence")
            else:
                require(isinstance(item, str) and item.strip(), f"{key}: empty {field}")
                if core:
                    require(item in {"Not reported", "Pending verification"}, f"{key}: missing map status")
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


def summary(records, core):
    included = sum(p["screening"] == "included" for p in records)
    return [f"**Survey in progress** · {len(core)} core biological studies · "
            f"{included} included works · {len(records)} records screened"]


def comparison(papers):
    lines = ["| Paper & venue | Scientific task | How it judges | Validation & key limit |", "|---|---|---|---|"]
    for p in papers:
        h = p["homepage"]
        links = [f"[Paper]({p['source']})"]
        if p.get("code"):
            links.append(f"[Code]({p['code']})")
        links.append(f"[Notes](docs/evidence.md#{p['id']})")
        role = {"A": "Judge method", "B": "Judge application"}[p["role"]]
        citation = f"**{h['name']}**<br>{h['venue']} {p['year']}<br>*{role}*<br>" + "&nbsp;·&nbsp;".join(links)
        cells = [citation, h["task"], h["method"], h["validation"]]
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def further_reading(records):
    lines = []
    for role in ("C", "D", "E"):
        papers = [p for p in records if p["role"] == role and p["screening"] == "included"]
        if not papers:
            continue
        name = f"{ROLES[role]} ({len(papers)})"
        lines += [f"<details><summary>{name}</summary>" if role == "C" else f"**{name}**", ""]
        for p in papers:
            lines += [f"- [{p['title']}]({p['url']}) — {p['contribution']} [Notes](docs/evidence.md#{p['id']})"]
        if role == "C":
            lines.extend(["", "</details>"])
        lines.append("")
    return lines


def detail(value):
    return value["detail"] if isinstance(value, dict) else value


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
            lines.append(f"- **{label}** — {detail(p['validation'][key])}")
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


def replace_block(original, lines, name="PAPER-LIST"):
    start, end = (f"<!-- {name}:{side} -->" for side in ("START", "END"))
    require(original.count(start) == original.count(end) == 1 and original.index(start) < original.index(end),
            f"Expected one ordered pair of {name} markers")
    before, after = original.split(start)
    return before + start + "\n\n" + "\n".join(lines).strip() + "\n\n" + end + after.split(end)[1]


def check_links(pages):
    for path, content in pages.items():
        for target in re.findall(r"\[[^\]]*\]\(([^ )]+)\)", content):
            if urlsplit(target).scheme:
                continue
            filename, _, anchor = target.partition("#")
            dest = (path.parent / filename).resolve() if filename else path
            require(dest.is_file() or dest in pages, f"{path.name}: missing {target}")
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
    core = [p for p in records if p["role"] in {"A", "B"} and p["screening"] == "included"]
    core.sort(key=lambda p: BRANCHES.index(p["homepage"]["branch"]))
    readme = ROOT / "README.md"
    page = readme.read_text(encoding="utf-8")
    for name, lines in [("SUMMARY", summary(records, core)), ("COMPARISON", comparison(core)),
                        ("PAPER-LIST", further_reading(records))]:
        page = replace_block(page, lines, name)
    pages = {readme: page}
    for filename, render in [("docs/evidence.md", evidence), ("docs/screening.md", screening)]:
        path = ROOT / filename
        pages[path] = replace_block(path.read_text(encoding="utf-8"), render(records))
    pages[ROOT / "assets/validation-map.svg"] = evidence_map(core)
    check_links(pages)
    for path, content in pages.items():
        if not path.exists() or content != path.read_text(encoding="utf-8"):
            require(not args.check, f"Stale output in {path.name}")
            path.write_text(content, encoding="utf-8")
    print(f"Validated {len(records)} records and {len(core)} core studies.")


if __name__ == "__main__":
    main()
