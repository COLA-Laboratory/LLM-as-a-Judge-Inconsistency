"""Editable, data-driven SVG figures for the survey homepage."""
from textwrap import wrap
from xml.etree import ElementTree as ET

BRANCH_TITLES = {
    "claim support": "Literature support for biological relationships",
    "hypothesis qualities": "Multidimensional quality of biological hypotheses",
    "research outputs": "Output quality of a drug-discovery assistant",
}
STUDY_TESTS = dict(repeat="Repeated calls", expert="Expert comparison",
                   perturbation="Controlled evidence perturbation", external="External relation labels")
FLOW = dict(object="Object", basis="Evidence or criteria", verdict="Judge output", use="Possible use")

INK, TEAL, PALE = "#183f42", "#17645f", "#dceee8"
MUTED, PAPER, GRAY = "#506469", "#fbfcfa", "#eef2f1"
GOLD, SAND = "#78571b", "#fff0cd"


class Figure:
    def __init__(self, title, height):
        self.root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", width="860",
                               height=str(height), viewBox=f"0 0 860 {height}", role="img")
        ET.SubElement(self.root, "title").text = title
        self.rect(0, 0, 860, height, PAPER, 10)

    def rect(self, x, y, w, h, fill, radius=0, **attrs):
        ET.SubElement(self.root, "rect", x=str(x), y=str(y), width=str(w), height=str(h),
                      fill=fill, rx=str(radius), **attrs)

    def text(self, x, y, value, size=16, color=INK, bold=False, center=False):
        attrs = {"font-family": "Arial, Helvetica, sans-serif", "font-size": str(size),
                 "font-weight": "700" if bold else "400", "fill": color,
                 "text-anchor": "middle" if center else "start"}
        ET.SubElement(self.root, "text", x=str(x), y=str(y), **attrs).text = value

    def lines(self, x, y, lines, **style):
        for i, value in enumerate(lines):
            self.text(x, y + i * 19, value, **style)

    def svg(self):
        ET.indent(self.root)
        return ET.tostring(self.root, encoding="unicode") + "\n"


def framework(papers):
    groups = []
    for key, title in BRANCH_TITLES.items():
        studies = []
        for paper in papers:
            home = paper["homepage"]
            if home["branch"] == key:
                cells = [wrap(home["flow"][k], width=23) for k in FLOW]
                height = max(map(len, cells)) * 19 + 36
                studies.append((f"{home['name']} · {home['venue']} {paper['year']}", cells, height))
        if studies:
            groups.append((title, studies))
    body_height = sum(46 + sum(row[2] for row in rows) for _, rows in groups)
    fig = Figure("Three biological judging tasks and their possible research uses", body_height + 101)
    for i, label in enumerate(FLOW.values()):
        fig.text(20 + i * 210, 27, label, bold=True, color=MUTED)
        if i < len(FLOW) - 1:
            fig.text(198 + i * 210, 27, "→", color=TEAL)
    y = 41
    for title, rows in groups:
        fig.rect(10, y, 840, 34, PALE, 5)
        fig.text(20, y + 23, title, 18, TEAL, bold=True)
        y += 34
        for citation, cells, height in rows:
            fig.text(20, y + 20, citation, 14, TEAL, bold=True)
            for i, lines in enumerate(cells):
                fig.lines(20 + 210 * i, y + 42, lines)
            y += height
        y += 12
    fig.rect(10, y, 840, 44, "#fffaf0", 5, stroke=GOLD, **{"stroke-dasharray": "5 4"})
    fig.text(20, y + 27, "Planned coverage", 16, GOLD, bold=True)
    fig.text(169, y + 27, "Judging experiment designs and prospectively prioritizing candidates.", 16)
    return fig.svg()


def evidence_map(papers):
    height = 120 + 65 * len(papers)
    fig = Figure("Tests performed on the judge in each core study", height)
    fig.text(16, 39, "Study", bold=True)
    for i, header in enumerate(STUDY_TESTS.values()):
        lines = wrap(header, width=19)
        fig.lines(260 + 167 * i, 38 - (len(lines) - 1) * 9, lines, bold=True, center=True)
    for i, paper in enumerate(papers):
        y = 62 + i * 65
        name = wrap(paper["homepage"]["name"], width=21)
        fig.lines(16, y + 34 - (len(name) - 1) * 9, name, size=14, bold=True)
        for col, key in enumerate(STUDY_TESTS):
            item = paper["validation"][key]
            if isinstance(item, dict):
                lines = [line for part in item["label"].split(" / ") for line in wrap(part, 18)]
                fill, color = PALE, TEAL
            elif item == "Pending verification":
                lines, fill, color = ["?"], SAND, GOLD
            else:
                lines, fill, color = ["—"], GRAY, MUTED
            x = 180 + 167 * col
            fig.rect(x, y, 160, 55, fill, 4)
            fig.lines(x + 80, y + 33 - (len(lines) - 1) * 9, lines, size=15,
                      bold=True, center=True, color=color)
    for x, symbol, fill, ink, label in [(16, "●", PALE, TEAL, "Reported"),
                                         (196, "—", GRAY, MUTED, "Not reported"),
                                         (389, "?", SAND, GOLD, "Pending verification")]:
        fig.rect(x, height - 40, 26, 24, fill, 4)
        fig.text(x + 13, height - 23, symbol, 15, ink, bold=True, center=True)
        fig.text(x + 34, height - 23, label, 15)
    return fig.svg()
