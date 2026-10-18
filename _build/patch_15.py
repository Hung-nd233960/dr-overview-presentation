# -*- coding: utf-8 -*-
import re


def edit(path, pairs):
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (path, a[:70])
        s = s.replace(a, b)
    open(path, 'w', encoding='utf-8').write(s)


# ---- tests
edit('test_engine.js', [
    ("chk([3, 3], 1.08, 100, 21.6, 178.4);", "chk([3, 3], 1.08, 100, 21.6, 178.4);\nchk([1.5, 6], 1.08, 100, 19.8, 180.2);\nchk([6, 1.5], 1.08, 100, 25.2, 174.8);"),
    ("near(res[0].score, 178.4);", "near(res[0].score, 180.2);"),
])

# ---- lab
edit('lab_template.html', [
    ("if(k>='1'&&k<='8')playCard(+k-1)", "if(k>='1'&&k<='9')playCard(+k-1)"),
    ("<span>&times;&frac12;</span><span>&times;2</span>", "<span>&times;&frac12;</span><span>&times;1.5</span><span>&times;2</span>"),
    ("so cards chain (&times;6 then &times;3 = &times;18 of the start)", "so cards chain (&times;6 then &times;1.5 = &times;9 of the start)"),
    ('<div><em>then &times;3</em><i style="width:108px"></i><u>= 18 &times; start</u></div>', '<div><em>then &times;1.5</em><i style="width:54px"></i><u>= 9 &times; start</u></div>'),
    (".card{position:relative;display:flex;align-items:center;justify-content:center;width:82px;height:116px;", ".card{position:relative;display:flex;align-items:center;justify-content:center;width:76px;height:116px;"),
    ("#cards{display:flex;gap:10px;margin:0}", "#cards{display:flex;gap:8px;margin:0}"),
])
# keys help text on the rules/details (if present)
t = open('lab_template.html', encoding='utf-8').read()
t = t.replace("<kbd>1</kbd>-<kbd>8</kbd>", "<kbd>1</kbd>-<kbd>9</kbd>")
open('lab_template.html', 'w', encoding='utf-8').write(t)

# ---- deck
d = open('build_deck.js', encoding='utf-8').read()
a = d.index("['×⅙', '×¼', '×⅓', '×½', '×2', '×3', '×4', '×6'].forEach")
b = d.index("\n", a)
line = "  ['×⅙', '×¼', '×⅓', '×½', '×1.5', '×2', '×3', '×4', '×6'].forEach((t, i) => box(s, 7.0 + i * 0.66, 4.7, 0.6, 0.6, t, { fill: WHITE, line: NAVY, size: 15, bold: true, margin: 0 }));"
d = d[:a].rstrip(' ') + line + d[b:]
d = d.replace("['then \\u00D73', 18, TEAL, '= 18 \\u00D7 start']", "['then \\u00D71.5', 9, TEAL, '= 9 \\u00D7 start']")
d = d.replace("(x6 then x3 = x18 of the start)", "(x6 then x1.5 = x9 of the start)")
open('build_deck.js', 'w', encoding='utf-8').write(d)
assert "×1.5" in d and "x1.5" in d

# ---- script
edit('script_data.py', [
    ("times six, then times three, is eighteen times the start", "times six, then times one and a half, is nine times the start"),
    ("×6 rồi ×3 là gấp 18 lần ban đầu", "×6 rồi ×1,5 là gấp 9 lần ban đầu"),
])

# ---- guide + checklist
g = open('../Knowledge_Guide.md', encoding='utf-8').read()
g = g.replace("×6 then ×3 = ×18 of the start", "×6 then ×1.5 = ×9 of the start")
g = g.replace("The best route is ×3 → ×3 = 1.08× (score 178.4).", "The best route is ×1.5 → ×6 = 1.08× (score 180.2); ×3 → ×3 reaches the same image for 178.4. **Order matters:** ×6 → ×1.5 reaches the same ×9 but scores only 174.8, because the intermediate scan costs more dose.")
g = g.replace("the cards are ×⅙, ¼, ⅓, ½, 2, 3, 4, 6", "the cards are ×⅙, ¼, ⅓, ½, 1.5, 2, 3, 4, 6")
g = re.sub(r"\*\*×3 → ×3 = 178\.4\*\*, ×¼ → ×6 → ×6 = 176\.9, ×2 → ×4 = 176\.8", "**×1.5 → ×6 = 180.2**, ×3 → ×3 = 178.4, ×¼ → ×6 → ×6 = 176.9 (then ×2 → ×4 = 176.8)", g)
open('../Knowledge_Guide.md', 'w', encoding='utf-8').write(g)
c = open('../Rehearsal_Checklist.md', encoding='utf-8').read()
c = c.replace("Expected best route: ×3 then ×3 (score 178.4).", "Expected best route: ×1.5 then ×6 (score 180.2); ×3 then ×3 scores 178.4.")
c = c.replace("printed cards (×⅙ … ×6)", "printed cards (×⅙ … ×6, including ×1.5)")
c = c.replace("keys `1`–`8` cards", "keys `1`–`9` cards")
open('../Rehearsal_Checklist.md', 'w', encoding='utf-8').write(c)
print('ok')
