# -*- coding: utf-8 -*-
import re


def edit(path, pairs, regex=False):
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        if regex:
            s2 = re.sub(a, b, s, flags=re.S)
            assert s2 != s, a[:60]
            s = s2
        else:
            assert a in s, (path, a[:70])
            s = s.replace(a, b)
    open(path, 'w', encoding='utf-8').write(s)


# ---------------- engine ----------------
edit('engine.js', [
    ("const CARDS = [1 / 6, 1 / 4, 1 / 3, 1 / 2, 2, 3, 4, 6];", "const CARDS = [2, 3, 4, 6, 8, 10, 15, 40]; // multiples of the INITIAL scan"),
    ("r *= CARDS[ci]; D += doseOf(r) + RETAKE; n++;", "r = r0 * CARDS[ci]; D += doseOf(r) + RETAKE; n++; // each card = a new scan at initial x card"),
])

e = open('engine.js', encoding='utf-8').read()
e = re.sub(r"const CARD_LABELS = \[.*?\];", "const CARD_LABELS = ['\u00D72', '\u00D73', '\u00D74', '\u00D76', '\u00D78', '\u00D710', '\u00D715', '\u00D740'];", e, count=1)
open('engine.js', 'w', encoding='utf-8').write(e)

# ---------------- test ----------------
s = open('test_engine.js', encoding='utf-8').read()
a = s.index('chk([], 0.12')
b = s.index('// exhaustive top-3')
s = s[:a] + """chk([], 0.12, 34.6, 1.2, 68.1);
chk([6], 0.72, 84.9, 11.4, 158.3);
chk([8], 0.96, 98.0, 13.8, 182.2);
chk([10], 1.2, 100, 16.2, 183.8);
chk([15], 1.8, 100, 22.2, 177.8);
chk([40], 4.8, 94.7, 52.2, 137.2);
chk([2, 10], 1.2, 100, 21.6, 178.4);
chk([4, 10], 1.2, 100, 24.0, 176.0);
""" + s[b:]
s = s.replace("near(res[0].score, 178.4);", "near(res[0].score, 183.8);")
open('test_engine.js', 'w', encoding='utf-8').write(s)
# test helper idx() uses E.CARDS.findIndex(x => |x-c|<1e-9): card values are now whole numbers, still fine

# ---------------- lab ----------------
edit('lab_template.html', [
    ("hist:[E.R0],seeds:[7]", "hist:[E.R0],cards:['start'],seeds:[7]"),
    ("T.r*=E.CARDS[ci];T.D+=E.doseOf(T.r)+E.RETAKE;T.hist.push(T.r);", "T.r=E.R0*E.CARDS[ci];T.D+=E.doseOf(T.r)+E.RETAKE;T.hist.push(T.r);T.cards.push(E.CARD_LABELS[ci]);"),
    ("T.hist.forEach((r,i)=>{const c=mk(120,120);drawTo(c,drImg(r,T.seeds[i]));h.appendChild(c)});",
     "T.hist.forEach((r,i)=>{const w=document.createElement('div');w.className='hi'+(i===T.hist.length-1?' last':'');const c=mk(120,120);drawTo(c,drImg(r,T.seeds[i]));w.appendChild(c);const sp=document.createElement('span');sp.textContent=T.cards[i];w.appendChild(sp);h.appendChild(w)});"),
    (".hist{display:flex;gap:6px;justify-content:flex-start;align-items:center}",
     ".hist{display:grid;grid-template-columns:repeat(3,58px);gap:4px 10px;justify-content:start}\n.hi{display:flex;flex-direction:column;align-items:center}\n.hi span{font-size:14px;font-weight:800;color:var(--ink);margin-top:1px;line-height:1.15}\n.hi.last canvas{border-color:var(--teal)}\n.hi.last span{color:var(--teal)}"),
    (".hist canvas:last-child{border-color:var(--teal)}", ""),
    (".row2{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:12px;min-height:56px}",
     ".row2{display:flex;align-items:flex-start;justify-content:center;gap:10px;margin-top:8px}\n.row2 .lbl{margin-top:16px}"),
    ("width:276px;height:276px", "width:224px;height:224px"),
    (".card{width:96px;height:68px;font-size:32px;", ".card{width:96px;height:56px;font-size:30px;"),
    ("#cards{display:flex;gap:14px;justify-content:center;margin:16px 0 10px}", "#cards{display:flex;gap:14px;justify-content:center;margin:6px 0 10px}\n#cardnote{text-align:center;font-size:17px;color:var(--mute);margin-top:12px}\n#cardnote b{color:var(--amber)}"),
    ('<div id="cards"></div>', '<div id="cardnote">Each card multiplies the <b>initial</b> scan, not your last scan</div>\n    <div id="cards"></div>'),
    # reveal captions
    ("(r*100).toFixed(0)+'% · DI '", "(T.cards[i]==='start'?'start':T.cards[i])+' → '+(r*100).toFixed(0)+'% · DI '"),
])
# rules screen
edit('lab_template.html', [
    (r'<span>Each round your team plays <b>one multiplier card</b>\..*?</span>',
     '<span>Each round your team plays <b>one multiplier card</b>. Your new scan = the <b>initial scan &times; card</b> (not your last scan &times; card): new image, more dose.</span>'),
    (r'<div class="rbox"><h3>Cards</h3>.*?</div></div>',
     '<div class="rbox"><h3>Cards: multiples of the <u>initial</u> scan</h3><div class="chips"><span>&times;2</span><span>&times;3</span><span>&times;4</span><span>&times;6</span><span>&times;8</span><span>&times;10</span><span>&times;15</span><span>&times;40</span></div>'
     '<div class="mdiag"><div><em>initial</em><i style="width:8px;background:var(--amber)"></i><u>1</u></div><div><em>play &times;6</em><i style="width:48px"></i><u>6 &times; initial</u></div><div><em>then &times;10</em><i style="width:80px"></i><u>10 &times; initial (not 60)</u></div></div></div>'),
    (".bar3{display:flex;", ".mdiag{margin-top:8px;font-size:15px}\n.mdiag div{display:flex;align-items:center;gap:8px;margin-top:3px}\n.mdiag em{width:82px;font-style:normal;color:var(--mute)}\n.mdiag i{display:block;height:12px;background:var(--teal);border-radius:3px}\n.mdiag u{text-decoration:none;color:var(--ink);font-weight:700}\n.bar3{display:flex;"),
], regex=False) if False else None
t = open('lab_template.html', encoding='utf-8').read()
t = re.sub(r'<span>Each round your team plays <b>one multiplier card</b>\..*?</span>',
           '<span>Each round your team plays <b>one multiplier card</b>. Your new scan = the <b>initial scan &times; card</b> (not your last scan &times; card): new image, more dose.</span>', t, count=1, flags=re.S)
t = re.sub(r'<div class="rbox"><h3>Cards</h3>.*?</div></div>',
           '<div class="rbox"><h3>Cards: multiples of the <u style="text-decoration:none;color:var(--ink)">initial</u> scan</h3><div class="chips"><span>&times;2</span><span>&times;3</span><span>&times;4</span><span>&times;6</span><span>&times;8</span><span>&times;10</span><span>&times;15</span><span>&times;40</span></div>'
           '<div class="mdiag"><div><em>initial</em><i style="width:8px;background:var(--amber)"></i><u>1</u></div><div><em>play &times;6</em><i style="width:48px"></i><u>6 &times; initial</u></div><div><em>then &times;10</em><i style="width:80px"></i><u>10 &times; initial (not 60)</u></div></div></div>',
           t, count=1, flags=re.S)
t = t.replace(".bar3{display:flex;", ".mdiag{margin-top:8px;font-size:15px}\n.mdiag div{display:flex;align-items:center;gap:8px;margin-top:3px}\n.mdiag em{width:82px;font-style:normal;color:var(--mute)}\n.mdiag i{display:block;height:12px;background:var(--teal);border-radius:3px}\n.mdiag u{text-decoration:none;color:var(--ink);font-weight:700}\n.bar3{display:flex;", 1)
open('lab_template.html', 'w', encoding='utf-8').write(t)

# ---------------- deck ----------------
edit('build_deck.js', [
    ("'Each round: play a × card on your own exposure. New image, more dose.'", "'Each round: play a × card. New scan = initial × card, not last scan × card.'"),
    ("['×⅙', '×¼', '×⅓', '×½', '×2', '×3', '×4', '×6']", "['×2', '×3', '×4', '×6', '×8', '×10', '×15', '×40']"),
])
d = open('build_deck.js', encoding='utf-8').read()
a = d.index("  txt(s, 'Dose bar (relative):'")
b = d.index("}\n", d.index("Open DR_Lab.html → tab 3', 7.0, 6.45"))
new = """  txt(s, 'Cards multiply the INITIAL scan, not your last scan', 7.0, 5.45, 5.8, 0.35, { size: 15, bold: true, color: NAVY });
  const rowsD = [['initial', 1, AMB, '1'], ['play \\u00D76', 6, TEAL, '6 \\u00D7 initial'], ['then \\u00D710', 10, TEAL, '10 \\u00D7 initial (not 60)']];
  rowsD.forEach((r, i) => {
    const y = 5.85 + i * 0.36;
    txt(s, r[0], 7.0, y - 0.03, 1.3, 0.3, { size: 14, color: MUTE, valign: 'middle' });
    s.addShape(pres.ShapeType.rect, { x: 8.35, y, w: 0.16 * r[1], h: 0.24, fill: { color: r[2] }, line: { color: r[2], width: 0.5 } });
    txt(s, r[3], 8.35 + 0.16 * r[1] + 0.12, y - 0.03, 3.2, 0.3, { size: 14, bold: true, color: INK, valign: 'middle' });
  });
"""
d = d[:a] + new + d[b:]
d = d.replace("'Images: simulated by the group from a CC0 chest radiograph (Wikimedia Commons); simplified model: noise \\u221D 1/\\u221Aphotons, dose \\u221D mAs (Seeram \\u00A71.3.5-1.3.6). DR_Lab.html, tab 3.'", "'Images: simulated by the group from a CC0 chest radiograph (Wikimedia Commons); simplified model: noise \\u221D 1/\\u221Aphotons, dose \\u221D mAs (Seeram \\u00A71.3.5-1.3.6). Run from DR_Lab.html, tab 3.'")
d = d.replace("Each round, a team plays a multiplier card on its own exposure; the new image appears for both teams, so they compare.", "Each round, a team plays a multiplier card; the new scan is the INITIAL exposure times the card (not the last scan times the card), so every card is a fresh scan and more dose. The new image appears for both teams, so they compare. Cards: x2 to x6 are still grainy, x8 and x10 land at about the ideal, x15 is wasteful overexposure that looks identical, x40 looks fine but blows the dose limit.")
open('build_deck.js', 'w', encoding='utf-8').write(d)

# ---------------- script / docs ----------------
edit('script_data.py', [
    ("Each round you play one multiplier card on your own exposure. You see your new image, and so does the other team.",
     "Each round you play one multiplier card. The card multiplies the initial exposure, not your last one: a times ten card means ten times the starting exposure, whatever you played before. Every card is a new scan, so a new image and more dose. Both teams see every image."),
    ("Mỗi vòng, đội chơi một thẻ nhân lên phơi sáng của mình. Ảnh mới hiện ra cho cả hai đội cùng xem.",
     "Mỗi vòng, đội chơi một thẻ nhân. Thẻ nhân lên phơi sáng BAN ĐẦU, không phải lần chụp trước: thẻ ×10 nghĩa là gấp mười lần phơi sáng ban đầu, bất kể trước đó đã chơi gì. Mỗi thẻ là một lần chụp mới, nên có ảnh mới và thêm liều. Ảnh mới hiện ra cho cả hai đội cùng xem."),
])
edit('../Rehearsal_Checklist.md', [
    ("(cost = 10 × exposure + 3 per card)", "(cost = 10 × the scan's exposure + 3, where the scan's exposure = initial × the card)"),
    ("printed cards (×⅙ … ×6)", "printed cards (×2 … ×40)"),
    ("Expected best route: ×3 then ×3 (score 178.4).", "Expected best play: a single ×10 (score 183.8), then ×8 (182.2). Overexposure traps: ×15 (looks fine, wasteful) and ×40 (looks fine, hits the dose limit)."),
])
g = open('../Knowledge_Guide.md', encoding='utf-8').read()
a = g.index("- **Dose** per exposure = 10·r")
b = g.index("- **Real limit of the model**")
g = g[:a] + """- **Dose** per scan = 10·r, **+3** fixed cost per retake (repositioning, time, extra exposure). The +3 stops "deliberately under-expose first" from being a free strategy.
- **Cards multiply the INITIAL scan, not the previous one.** Each card is a fresh scan at r = r₀ × card (r₀ = 1/8.33 ≈ 0.12), so playing ×6 and then ×10 gives 10 × r₀ = 1.2, not 60 × r₀. Fractions (×½ and below) were removed: they could only make the image worse.
- **Cards:** ×2, ×3, ×4, ×6, ×8, ×10, ×15, ×40 → r = 0.24, 0.36, 0.48, 0.72, 0.96, 1.20, 1.80, 4.80. ×2–×6 are visibly grainy; ×8 (r = 0.96, Q 98) and ×10 (r = 1.2, Q 100) land near the ideal; ×15 is **overexposure that looks identical** but costs more dose; ×40 also looks fine yet pushes dose past the limit (the team is stopped).
- **Why no exact route exists**: the ideal needs ×8.33. ×8 is just under (small grain, Q 98), ×10 just over (clean, slightly more dose). Real trade-off.
- **Verified single-scan scores** (exhaustive simulation of all sequences ≤ 4 cards, `_build/test_engine.js`): ×10 = **183.8**, ×8 = 182.2, ×15 = 177.8, ×6 = 158.3, ×40 = 137.2. Best multi-scan: ×2 → ×10 = 178.4 (the exploratory scan costs ≈ 5 points). Lesson: the cheapest route is to read the grain, then pick the smallest card that looks clean, in one scan.
""" + g[b:]
g = g.replace("- **Quality** Q(r) = 100·√r for r < 1", "- **Quality** Q(r) = 100·√r for r < 1")
open('../Knowledge_Guide.md', 'w', encoding='utf-8').write(g)
print('all patched')
