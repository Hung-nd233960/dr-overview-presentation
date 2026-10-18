# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()

# ---------- CSS ----------
a = t.index('#bj .top{')
b = t.index('#reveal{display:none}')
css = """
#bjGame{max-width:1240px;margin:0 auto}
.statusbar{display:flex;align-items:center;justify-content:center;gap:16px;margin:2px 0 12px}
.pill{background:var(--navy);border:2px solid var(--teal);border-radius:999px;padding:4px 18px;font-size:19px;font-weight:700;color:var(--teal);white-space:nowrap}
.status{font-size:23px;font-weight:600;text-align:center}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px;align-items:start}
.team,.ideal{background:var(--panel);border:3px solid #223a5a;border-radius:16px;padding:12px 14px 14px;text-align:center;transition:border-color .2s,box-shadow .2s}
.team.act{border-color:var(--teal);box-shadow:0 0 0 4px rgba(31,181,168,.22)}
.team.stand{opacity:.72}
.team h2,.ideal h2{margin:0 0 10px;font-size:23px;letter-spacing:.5px}
.team.act h2::after{content:'  \\25B8 playing';color:var(--teal);font-size:16px;font-weight:600}
.team.stand h2::after{content:'  \\00B7 done';color:var(--mute);font-size:16px;font-weight:600}
.ideal h2{color:var(--amber)}
.team canvas,.ideal canvas{margin:0 auto;border-radius:8px;box-shadow:0 4px 18px rgba(0,0,0,.45)}
.row2{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:12px;min-height:56px}
.lbl{font-size:14px;color:var(--mute);min-width:52px;text-align:right}
.hist{display:flex;gap:6px;justify-content:flex-start;align-items:center}
.hist canvas{width:50px;height:50px;border:2px solid #2c4468;border-radius:5px;box-shadow:none}
.hist canvas:last-child{border-color:var(--teal)}
.dosewrap{display:flex;align-items:center;gap:10px;margin-top:10px}
.dose{flex:1;height:20px;border-radius:10px;background:#0a1322;overflow:hidden;border:1px solid #2c4468}
.dose i{display:block;height:100%;width:0;background:var(--green);transition:width .5s,background .3s}
.roundbig{font-size:17px;color:var(--mute);margin-top:12px;min-height:56px;display:flex;align-items:center;justify-content:center}
#coinbar{display:none;justify-content:center;align-items:center;gap:14px;margin:16px 0 4px;font-size:21px}
#coinbar button{font-size:19px}
#cards{display:flex;gap:14px;justify-content:center;margin:18px 0 12px}
.card{width:96px;height:68px;font-size:32px;border-radius:12px;background:#f4f7fb;color:#12304a;border:3px solid #fff;font-weight:800;cursor:pointer;transition:transform .1s,box-shadow .1s;box-shadow:0 3px 10px rgba(0,0,0,.35)}
.card:hover:not(.used){transform:translateY(-4px);box-shadow:0 8px 16px rgba(0,0,0,.45)}
.card.used{background:#3a4658;color:#6c7a90;border-color:#3a4658;text-decoration:line-through;cursor:not-allowed;box-shadow:none}
#bj .btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
/* rules screen */
#bjRules{max-width:1060px;margin:6px auto 0;background:var(--panel);border:2px solid #223a5a;border-radius:18px;padding:22px 34px 26px}
#bjRules h1{margin:0;font-size:36px;color:var(--teal)}
#bjRules .goal{font-size:21px;margin:6px 0 16px;color:var(--ink)}
.rgrid{display:grid;grid-template-columns:1.25fr 1fr;gap:30px}
.rule{display:flex;gap:14px;align-items:flex-start;margin-bottom:12px;font-size:19px;line-height:1.3}
.rule b.n{flex:none;width:34px;height:34px;border-radius:50%;background:var(--teal);color:#06231f;display:flex;align-items:center;justify-content:center;font-size:19px}
.rbox{background:#0f1b2d;border-radius:12px;padding:14px 18px;margin-bottom:14px;font-size:18px;line-height:1.35}
.rbox h3{margin:0 0 6px;font-size:19px;color:var(--amber)}
.rbox .big{font-size:24px;color:var(--ink)}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
.chips span{background:#f4f7fb;color:#12304a;border-radius:8px;padding:2px 9px;font-weight:800;font-size:19px}
.bar3{display:flex;height:14px;border-radius:7px;overflow:hidden;margin-top:8px}
.bar3 i{flex:1}
#proceed{display:block;margin:12px auto 0;font-size:24px;padding:12px 40px}
.proceedhint{text-align:center;color:var(--mute);font-size:14px;margin-top:8px}
"""
t = t[:a] + css.strip('\n') + '\n' + t[b:]

# ---------- HTML ----------
a = t.index('<section id="bj">')
b = t.index('</section>', a) + len('</section>')
html = """<section id="bj">
  <div id="bjRules">
    <h1>X-ray Blackjack</h1>
    <div class="goal">Make your image match the <b style="color:var(--amber)">IDEAL</b> as closely as you can, using as <b>little dose</b> as possible.</div>
    <div class="rgrid">
      <div>
        <div class="rule"><b class="n">1</b><span>Both teams start from the <b>same grainy image</b>. The ideal image stays on screen.</span></div>
        <div class="rule"><b class="n">2</b><span>Each round your team plays <b>one multiplier card</b>. It multiplies your exposure: new image, more dose. Both teams see every image.</span></div>
        <div class="rule"><b class="n">3</b><span><b>No copying:</b> the card the first team plays is blocked for the second team that round. The first pick alternates.</span></div>
        <div class="rule"><b class="n">4</b><span>Up to <b>4 rounds</b>. Say <b>STAND</b> any time you think you are close enough.</span></div>
        <div class="rule"><b class="n">5</b><span>Your <b>last image</b> is your submission, not your best one.</span></div>
      </div>
      <div>
        <div class="rbox"><h3>Scoring</h3><div class="big">Score = Quality &times; 2 &minus; Dose</div>Quality stays <b>hidden</b> until the end: judge it with your eyes. Higher score wins.</div>
        <div class="rbox"><h3>Cards</h3>Each card multiplies your own exposure.<div class="chips"><span>&times;&#8537;</span><span>&times;&frac14;</span><span>&times;&#8531;</span><span>&times;&frac12;</span><span>&times;2</span><span>&times;3</span><span>&times;4</span><span>&times;6</span></div></div>
        <div class="rbox"><h3>Dose bar</h3>Relative, no numbers. Green &rarr; amber &rarr; red. When it is full, you are stopped.<div class="bar3"><i style="background:var(--green)"></i><i style="background:var(--amber)"></i><i style="background:var(--red)"></i></div></div>
      </div>
    </div>
    <button id="proceed">Proceed to play &#9654;</button>
    <div class="proceedhint">or press <kbd>Enter</kbd></div>
  </div>
  <div id="bjGame" style="display:none">
    <div class="statusbar"><span class="pill" id="roundPill">Round 1 / 4</span><div class="status" id="bjStatus"></div></div>
    <div class="grid3">
      <div class="team" id="tL"><h2>TEAM LEFT</h2><canvas id="cL" width="768" height="768" style="width:290px;height:290px"></canvas>
        <div class="row2"><span class="lbl">History</span><div class="hist" id="hL"></div></div>
        <div class="dosewrap"><span class="lbl">Dose</span><div class="dose"><i id="dL"></i></div></div></div>
      <div class="ideal"><h2>IDEAL</h2><canvas id="cI" width="768" height="768" style="width:290px;height:290px"></canvas>
        <div class="roundbig" id="roundInfo">Match this image with as little dose as possible</div></div>
      <div class="team" id="tR"><h2>TEAM RIGHT</h2><canvas id="cR" width="768" height="768" style="width:290px;height:290px"></canvas>
        <div class="row2"><span class="lbl">History</span><div class="hist" id="hR"></div></div>
        <div class="dosewrap"><span class="lbl">Dose</span><div class="dose"><i id="dR"></i></div></div></div>
    </div>
    <div id="coinbar"><span>Who picks first in round 1?</span><button class="sec" id="coinL">Team Left</button><button id="coinF">Flip a coin</button><button class="sec" id="coinR">Team Right</button></div>
    <div id="cards"></div>
    <div class="btns">
      <button id="standBtn" class="sec">STAND <kbd>S</kbd></button>
      <button class="sec" id="undo">Undo <kbd>U</kbd></button>
      <button id="reveal">Reveal <kbd>V</kbd></button>
      <button class="sec" id="rulesBtn">Rules</button>
      <button class="sec" id="newgame">New game <kbd>N</kbd></button>
    </div>
    <div id="revealbox"></div>
  </div>
</section>"""
t = t[:a] + html + t[b:]

# ---------- JS ----------
def rep(old, new):
    global t
    assert old in t, old[:60]
    t = t.replace(old, new)

rep("$('#roundInfo').textContent=S.over||!S.first?'':'Round '+S.round+' / 4';",
    "$('#roundPill').textContent=S.over?'Game over':'Round '+Math.min(S.round,4)+' / 4';$('#roundInfo').textContent=S.over?'Press Reveal to see the quality scores':(S.first?'Match this image with as little dose as possible':'Match this image with as little dose as possible');")
rep("$('#standBtn').disabled=!t;$('#coinL').style.display=$('#coinR').style.display=S.first?'none':'';",
    "$('#standBtn').disabled=!t;$('#coinbar').style.display=S.first?'none':'flex';")
rep("$('#coinL').onclick=()=>setFirst('L');$('#coinR').onclick=()=>setFirst('R');",
    "$('#coinL').onclick=()=>setFirst('L');$('#coinR').onclick=()=>setFirst('R');$('#coinF').onclick=()=>setFirst(Math.random()<.5?'L':'R');\n"
    "let rulesOn=true;\nfunction showRules(on){rulesOn=on;$('#bjRules').style.display=on?'block':'none';$('#bjGame').style.display=on?'none':'block'}\n"
    "$('#proceed').onclick=()=>showRules(false);$('#rulesBtn').onclick=()=>showRules(true);")
rep("  else if(cur==='bj'){\n    if(k>='1'",
    "  else if(cur==='bj'&&rulesOn){if(k==='enter'||k===' ')showRules(false)}\n  else if(cur==='bj'){\n    if(k>='1'")
rep("else if(k==='l'&&!S.first)setFirst('L');else if(k==='r'&&!S.first)setFirst('R');",
    "else if(k==='l'&&!S.first)setFirst('L');else if(k==='r'&&!S.first)setFirst('R');else if(k==='f'&&!S.first)setFirst(Math.random()<.5?'L':'R');")
open('lab_template.html', 'w', encoding='utf-8').write(t)
print('patched')
