"""Builds app/index.html from data/cards.jsonl + data/explanations.py + app/template.html."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
cards = [json.loads(l) for l in (root / "data/cards.jsonl").read_text().splitlines() if l.strip()]
ns = {}
exec((root / "data/explanations.py").read_text(), ns)
E = ns["E"]
assert len(E) == len(cards), (len(E), len(cards))
out = []
for i, (c, (expl, fig)) in enumerate(zip(cards, E), 1):
    d = {"id": f"c{i:03d}", "q": c["q"], "a": c["a"], "o": c["o"], "e": expl, "src": c["src"]}
    if fig: d["fig"] = fig
    out.append(d)
tpl = (root / "app/template.html").read_text()
html = tpl.replace("/*__CARDS__*/[]", json.dumps(out, ensure_ascii=False))
(root / "app/index.html").write_text(html)
print(len(out), "cards,", len(html) // 1024, "KB")
