# -*- coding: utf-8 -*-
import re


def sub(s, pat, repl, flags=re.S):
    s2 = re.sub(pat, repl, s, count=1, flags=flags)
    assert s2 != s, pat[:60]
    return s2


# ---------------- lab ----------------
t = open('lab_template.html', encoding='utf-8').read()
t = t.replace("T.r=E.R0*E.CARDS[ci];", "T.r*=E.CARDS[ci];")
assert "T.r*=E.CARDS[ci]" in t

t = sub(t, r'<span>Each round your team plays <b>one multiplier card</b>\..*?</span>',
        '<span>Each round your team plays <b>one multiplier card</b>. It multiplies the exposure of your <b>last scan</b>, so cards <b>chain</b>: new image, more dose. Both teams see every image.</span>')
t = sub(t, r'<div class="rbox"><h3>Cards:.*?</div></div>',
        '<div class="rbox"><h3>Cards chain on your last scan</h3><div class="chips"><span>&times;&#8537;</span><span>&times;&frac14;</span><span>&times;&#8531;</span><span>&times;&frac12;</span><span>&times;2</span><span>&times;3</span><span>&times;4</span><span>&times;6</span></div>'
        '<div class="mdiag"><div><em>start</em><i style="width:6px;background:var(--amber)"></i><u>1</u></div><div><em>play &times;6</em><i style="width:36px"></i><u>= 6 &times; start</u></div><div><em>then &times;3</em><i style="width:108px"></i><u>= 18 &times; start</u></div></div></div>')
t = t.replace('<div id="cardnote">Each card multiplies the <b>initial</b> scan, not your last scan</div>',
              '<div id="cardnote">Each card multiplies your <b>last</b> scan, so cards chain (&times;6 then &times;3 = &times;18 of the start)</div>')

# 4th column: START image, shown once any team has played a card
t = t.replace('<div class="ideal"><h2>IDEAL</h2>',
              '<div class="ideal" id="tS" style="display:none"><h2 style="color:var(--mute)">START</h2><canvas id="cS" width="768" height="768" style="width:204px;height:204px"></canvas>\n        <div class="roundbig">Where both teams began</div></div>\n      <div class="ideal"><h2>IDEAL</h2>', 1)
assert 'id="tS"' in t
t = t.replace(".grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px;align-items:start}",
              ".grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px;align-items:start}\n.grid3.g4{grid-template-columns:repeat(4,1fr);gap:14px}")
assert '.g4' in t
t = t.replace("drawTo($('#cI'),baseImg);",
              "drawTo($('#cI'),baseImg);\n  {const any=S.T.L.hist.length>1||S.T.R.hist.length>1;$('#tS').style.display=any?'':'none';document.querySelector('.grid3').classList.toggle('g4',any);if(any)drawTo($('#cS'),drImg(S.T.L.hist[0],S.T.L.seeds[0]))}", 1)
assert "#cS" in t
open('lab_template.html', 'w', encoding='utf-8').write(t)

# ---------------- deck: slide 11 ----------------
d = open('build_deck.js', encoding='utf-8').read()
d = d.replace("'Each round: play a × card on your own exposure. New image, more dose.'", "'Each round: play a × card. It multiplies your last scan, so cards chain.'")
a = d.index("  txt(s, 'Dose bar (relative):'")
b = d.index("}\n", d.index("Open DR_Lab.html → tab 3', 7.0, 6.45"))
new = """  txt(s, 'Cards chain on your last scan', 7.0, 5.45, 5.8, 0.35, { size: 15, bold: true, color: NAVY });
  const rowsD = [['start', 1, AMB, '1'], ['play \\u00D76', 6, TEAL, '= 6 \\u00D7 start'], ['then \\u00D73', 18, TEAL, '= 18 \\u00D7 start']];
  rowsD.forEach((r, i) => {
    const y = 5.85 + i * 0.36;
    txt(s, r[0], 7.0, y - 0.03, 1.3, 0.3, { size: 14, color: MUTE, valign: 'middle' });
    s.addShape(pres.ShapeType.rect, { x: 8.35, y, w: 0.1 * r[1], h: 0.24, fill: { color: r[2] }, line: { color: r[2], width: 0.5 } });
    txt(s, r[3], 8.35 + 0.1 * r[1] + 0.12, y - 0.03, 3.2, 0.3, { size: 14, bold: true, color: INK, valign: 'middle' });
  });
"""
d = d[:a] + new + d[b:]
d = d.replace("Each round, a team plays a multiplier card on its own exposure; the new image appears for both teams, so they compare.", "Each round, a team plays a multiplier card on its own last scan, so cards chain (x6 then x3 = x18 of the start). The new image appears for both teams, so they compare; once anyone has played, the START image appears as a reference column.")
open('build_deck.js', 'w', encoding='utf-8').write(d)

# ---------------- script / docs ----------------
s = open('script_data.py', encoding='utf-8').read()
old = "Each round you play one multiplier card on your own exposure. You see your new image, and so does the other team."
assert old in s
s = s.replace(old, "Each round you play one multiplier card. It multiplies your last scan, so cards chain: times six, then times three, is eighteen times the start. You see your new image, and so does the other team. Once anyone has played, the original grainy image appears in a fourth column so you can judge how far you have come.")
old = "Mỗi vòng, đội chơi một thẻ nhân lên phơi sáng của mình. Ảnh mới hiện ra cho cả hai đội cùng xem."
assert old in s
s = s.replace(old, "Mỗi vòng, đội chơi một thẻ nhân. Thẻ nhân lên phơi sáng của lần chụp gần nhất, nên các thẻ cộng dồn: ×6 rồi ×3 là gấp 18 lần ban đầu. Ảnh mới hiện ra cho cả hai đội cùng xem. Khi có đội đã chơi, ảnh nhiễu ban đầu hiện ở cột thứ tư để mọi người so sánh mức tiến bộ.")
open('script_data.py', 'w', encoding='utf-8').write(s)

g = open('../Knowledge_Guide.md', encoding='utf-8').read()
old = "- **Dose** per exposure = 10·r"
assert old in g
g = g.replace(old, "- **Cards chain:** each card multiplies the team's *last* scan, so ×6 then ×3 = ×18 of the start. This makes the game less predictable than a lookup of \"initial × card\" and keeps the fractional cards useful for correcting an overshoot. The **START image** appears as a reference column once any team has played, and each team's **history** shows the multiplier used under every image.\n" + old, 1)
open('../Knowledge_Guide.md', 'w', encoding='utf-8').write(g)

c = open('../Rehearsal_Checklist.md', encoding='utf-8').read()
c = c.replace("(cost = 10 × exposure + 3 per card)", "(cost = 10 × exposure of that scan + 3; cards chain on the last scan)")
open('../Rehearsal_Checklist.md', 'w', encoding='utf-8').write(c)
print('ok')
