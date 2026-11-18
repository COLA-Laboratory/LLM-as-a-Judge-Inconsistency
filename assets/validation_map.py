"""Draw the reporting matrix using the same core records as the reading guide."""
from textwrap import wrap
from xml.etree import ElementTree as ET

COLUMNS = {
    "repeat": ("Repeat", "consistency"),
    "expert": ("Expert", "comparison"),
    "literature": ("Literature", "checks"),
    "experimental": ("Biological", "experiment"),
    "decision": ("Decision or", "efficiency"),
}
STYLES = {
    "reported": ("#d8ede7", "#124e45", "Reported"),
    "Not reported": ("#f2f4f4", "#536369", "Not reported"),
    "Pending verification": ("#fff0cd", "#79530d", "Pending verification"),
}


def evidence_map(papers):
    width = 860
    height = 126 + 48 * len(papers)
    root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", width=str(width),
                      height=str(height), viewBox=f"0 0 {width} {height}", role="img")
    ET.SubElement(root, "title").text = "Validation endpoints reported by each core study"

    def box(x, y, w, h, color, radius=4):
        ET.SubElement(root, "rect", x=str(x), y=str(y), width=str(w), height=str(h),
                      rx=str(radius), fill=color)

    def text(x, y, value, size=16, bold=False, center=False, color="#173b40"):
        attrs = {"font-family": "Arial, Helvetica, sans-serif", "font-size": str(size),
                 "font-weight": "700" if bold else "400", "fill": color,
                 "text-anchor": "middle" if center else "start"}
        ET.SubElement(root, "text", x=str(x), y=str(y), **attrs).text = value

    box(0, 0, width, height, "#fbfcfb", 10)
    text(17, 46, "Study", bold=True)
    for col, labels in enumerate(COLUMNS.values()):
        x = 180 + 133 * col + 64
        for line, label in enumerate(labels):
            text(x, 30 + 20 * line, label, bold=True, center=True)
    for i, paper in enumerate(papers):
        y = 64 + 48 * i
        labels = wrap(paper["homepage"]["name"], width=21)
        for line, label in enumerate(labels):
            text(17, y + 25 - (len(labels) - 1) * 9 + line * 18, label, size=14, bold=True)
        for col, key in enumerate(COLUMNS):
            cell = paper["validation"][key]
            if isinstance(cell, dict):
                status, label = cell["status"], cell["label"]
            else:
                status = cell
                label = "—" if status == "Not reported" else "?"
            fill, ink, _ = STYLES[status]
            x = 180 + 133 * col
            box(x, y, 128, 40, fill)
            text(x + 64, y + 26, label, size=15, bold=True, center=True, color=ink)
    for x, (status, (fill, ink, name)) in zip((18, 186, 378), STYLES.items()):
        y = height - 40
        box(x, y, 28, 24, fill)
        symbol = {"reported": "●", "Not reported": "—", "Pending verification": "?"}[status]
        text(x + 14, y + 17, symbol, 15, True, True, ink)
        text(x + 36, y + 17, name, 15)
    ET.indent(root)
    return ET.tostring(root, encoding="unicode") + "\n"
