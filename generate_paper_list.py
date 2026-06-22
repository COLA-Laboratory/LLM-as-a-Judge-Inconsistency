#!/usr/bin/env python3
"""Generate the Paper List section of README.md from papers.yaml.

Reads papers.yaml, groups entries by category, renders Markdown, and
injects it between the PAPER-LIST:START / PAPER-LIST:END markers in
README.md. Run from the repo root:

    python generate_paper_list.py
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: pip install pyyaml")

ROOT = Path(__file__).parent
PAPERS = ROOT / "papers.yaml"
README = ROOT / "README.md"

START = "<!-- PAPER-LIST:START -->"
END = "<!-- PAPER-LIST:END -->"

# Defines section order and the only valid category values.
CATEGORY_ORDER = [
    "Surveys",
    "Position / Order Bias",
    "Self-Preference Bias",
    "Length / Verbosity Bias",
    "Non-Transitivity",
    "Stability & Self-Consistency",
    "Calibration & Reliability",
    "Aggregation Models",
    "Mitigation & Repair",
]


def badge(label, value, color):
    label = label.replace("-", "--").replace(" ", "_")
    value = value.replace("-", "--").replace(" ", "_")
    return f"https://img.shields.io/badge/{label}-{value}-{color}.svg"


def render_entry(p):
    title = p["title"]
    url = p["url"]
    date = p.get("date", "")
    line = f"* [{title}]({url})"
    if date:
        line += f" ![date]({badge('date', date, 'b31b1b')})"
    if p.get("code"):
        line += f" [![code]({badge('code', 'link', 'black')})]({p['code']})"
    out = [line]
    if p.get("tldr"):
        out.append(f"  > {p['tldr']}")
    return "\n".join(out)


def main():
    papers = yaml.safe_load(PAPERS.read_text(encoding="utf-8")) or []

    valid = set(CATEGORY_ORDER)
    groups = {c: [] for c in CATEGORY_ORDER}
    for p in papers:
        cat = p.get("category")
        if cat not in valid:
            sys.exit(f"Unknown category {cat!r} in entry: {p.get('title')}")
        groups[cat].append(p)

    blocks = []
    total = 0
    for cat in CATEGORY_ORDER:
        entries = groups[cat]
        if not entries:
            continue
        entries.sort(key=lambda p: p.get("date", ""))
        total += len(entries)
        blocks.append(f"### {cat} ({len(entries)})\n")
        blocks.append("\n\n".join(render_entry(p) for p in entries))
        blocks.append("")  # blank line between sections

    body = "\n".join(blocks).strip()
    section = f"{START}\n\n{body}\n\n{END}"

    text = README.read_text(encoding="utf-8")
    pre, _, rest = text.partition(START)
    _, _, post = rest.partition(END)
    README.write_text(pre + section + post, encoding="utf-8")

    print(f"Wrote {total} papers across "
          f"{sum(1 for c in CATEGORY_ORDER if groups[c])} sections.")


if __name__ == "__main__":
    main()
