# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()


def rep(a, b):
    global t
    assert a in t, a[:70]
    t = t.replace(a, b)


# 1) hitting the dose limit = that team STANDS immediately (other team keeps playing)
rep("if(T.D>=E.LIMIT)T.stopped=true;",
    "if(T.D>=E.LIMIT){T.stand=true;T.stopped=true;toast('\\u26A0 Dose limit reached: '+(t==='L'?'Team Left':'Team Right')+' STANDS')}")
rep("(S.T[o].stand?' stood':' hit the dose limit')", "(S.T[o].stopped?' hit the dose limit and stands':' stood')")

# 2) warning line under the cards
rep('    <div id="cards"></div>\n    <div class="ctrls">',
    '    <div class="cardcol"><div id="cards"></div>\n    <div id="dosewarn">&#9888; Stronger multiplier = more added dose: each scan adds about 10 &times; its exposure (+3), and dose never goes down.</div></div>\n    <div class="ctrls">')
css = """
.cardcol{display:flex;flex-direction:column;align-items:center;gap:8px}
#dosewarn{font-size:15px;font-weight:600;color:var(--amber);text-align:center;white-space:nowrap}
.playbar{margin-top:8px}
"""
rep("</style>", css + "</style>")
t = t.replace('width:268px;height:268px', 'width:254px;height:254px')

# 3) rules screen
rep("Relative, no numbers. Green &rarr; amber &rarr; red. When it is full, you are stopped.",
    "Relative, no numbers. Green &rarr; amber &rarr; red. A stronger multiplier adds more dose. When it is full, your team <b>STANDS at once</b>; the other team keeps playing.")
open('lab_template.html', 'w', encoding='utf-8').write(t)

# 4) docs
g = open('../Knowledge_Guide.md', encoding='utf-8').read()
old = "- **Dose** per scan = 10·r"
if old in g:
    g = g.replace(old, "- **Dose limit = 50 (relative):** a team whose cumulative dose reaches it **STANDS immediately** (its last image is the submission); the other team keeps playing. Dose per scan is 10 × the scan's exposure + 3, so a stronger card adds more dose, and the same card costs more when stacked on an already high exposure; dose never decreases, even with a ×½ card.\n" + old, 1)
else:
    g += "\n- **Dose limit = 50 (relative):** a team that reaches it STANDS immediately; the other team keeps playing.\n"
open('../Knowledge_Guide.md', 'w', encoding='utf-8').write(g)

s = open('script_data.py', encoding='utf-8').read()
old = "If one team stands, the other keeps playing its remaining rounds, so standing early gains nothing."
assert old in s
s = s.replace(old, old + " If a team's dose bar fills up, that team stands at once too.")
old_vi = "nên dừng sớm không có lợi thế."
assert old_vi in s
s = s.replace(old_vi, old_vi + " Nếu thanh liều của một đội đầy, đội đó cũng dừng ngay.")
open('script_data.py', 'w', encoding='utf-8').write(s)

c = open('../Rehearsal_Checklist.md', encoding='utf-8').read()
c = c.replace("dose-bar colour)", "dose-bar colour; a full dose bar = that team STANDS, the other keeps playing)")
open('../Rehearsal_Checklist.md', 'w', encoding='utf-8').write(c)
print('ok')
