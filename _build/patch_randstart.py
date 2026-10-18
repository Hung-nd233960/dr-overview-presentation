# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()


def rep(a, b, count=None):
    global t
    assert a in t, a[:70]
    t = t.replace(a, b) if count is None else t.replace(a, b, count)


rep("r:E.R0,D:E.doseOf(E.R0),hist:[E.R0],cards:['start'],seeds:[7]", "r:R0g,D:E.doseOf(R0g),hist:[R0g],cards:['start'],seeds:[SEEDg]")
assert t.count("seeds:[SEEDg]") == 2
rep("T.seeds.push(S.round*10+(t==='L'?1:2))", "T.seeds.push(SEEDg+S.round*10+(t==='L'?1:2))")
rep("function newState(){",
    "// random start per game (same for both teams): 0.08-0.16x of the ideal exposure, fresh noise pattern.\n"
    "// ?r0=0.12 fixes it for rehearsal/testing.\n"
    "let R0g=E.R0,SEEDg=7;\n"
    "function randStart(){const q=new URLSearchParams(location.search);const f=parseFloat(q.get('r0'));R0g=f>0?f:Math.round((0.08+Math.random()*0.08)*1000)/1000;SEEDg=Math.floor(Math.random()*900000)+100;}\n"
    "function newState(){")
rep("function bjNew(){S=newState();", "function bjNew(){randStart();S=newState();")
rep("The ideal image stays on screen.</span>", "The ideal image stays on screen. The start is <b>different every game</b>.</span>")
open('lab_template.html', 'w', encoding='utf-8').write(t)

g = open('../Knowledge_Guide.md', encoding='utf-8').read()
old = "- **Why no exact route exists**"
if old not in g:
    old = "- **Why no exact 1× route exists**"
assert old in g
g = g.replace(old, "- **Random start (current behaviour):** every game draws a new start exposure r₀ uniformly from 0.08–0.16× of the ideal (about ×6.25–×12.5 away) and a new noise pattern, the same for both teams, so an example run cannot be memorised. Open the lab with `?r0=0.12` to fix the start at ≈ 1/8.33 for rehearsal; the numbers quoted below (best route ×1.5 → ×6 = 180.2, etc.) are for that fixed start.\n" + old, 1)
open('../Knowledge_Guide.md', 'w', encoding='utf-8').write(g)

c = open('../Rehearsal_Checklist.md', encoding='utf-8').read()
c = c.replace("Expected best route: ×1.5 then ×6 (score 180.2); ×3 then ×3 scores 178.4.",
              "The start is random every game (0.08–0.16× of ideal), so there is no fixed best route; for a predictable rehearsal open `DR_Lab.html?tab=bj&r0=0.12` (best route ×1.5 then ×6 = 180.2; ×3 then ×3 = 178.4).")
open('../Rehearsal_Checklist.md', 'w', encoding='utf-8').write(c)
print('ok', 'random every game' in c)
