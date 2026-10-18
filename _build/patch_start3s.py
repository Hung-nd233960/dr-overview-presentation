# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()

# ---- replace countdownFirst + spinFirst with one 3-second start sequence ----
a = t.index("// manual pick: 3-2-1 before the game (and the clock) starts")
b = t.index("// ---------- clocks: 30 s per turn")
new_js = r"""// Start sequence: exactly 3.0 s either way, shown in the CURRENT SIDE box, then the game (and clock) starts.
//  - manual pick: 3 - 2 - 1 for the chosen team
//  - Random: LEFT/RIGHT flip with decaying speed and land on the winner at 3.0 s
const START_MS=3000;
function sideShow(side,txt,sec){const sb=$('#sideBox');sb.className='cbox starting';sb.dataset.side=side;$('#sideTxt').textContent=txt;$('#sideSec').textContent=sec;$('#sideBar').style.width='0';$('#tL').classList.toggle('spin',side==='L');$('#tR').classList.toggle('spin',side==='R')}
function startSeq(mode,team){
  if(spinning||S.first||S.over)return;
  spinning=true;['coinL','coinR','coinF'].forEach(i=>$('#'+i).disabled=true);
  const end=()=>{['L','R'].forEach(x=>$('#t'+x).classList.remove('spin'));$('#sideBox').classList.remove('starting');['coinL','coinR','coinF'].forEach(i=>$('#'+i).disabled=false);spinning=false;setFirst(team)};
  const nm=x=>x==='L'?'LEFT':'RIGHT';
  const t0=performance.now();
  if(mode==='manual'){
    $('#bjStatus').textContent=(team==='L'?'Team Left':'Team Right')+' goes first — get ready';
    [3,2,1].forEach((n,k)=>setTimeout(()=>sideShow(team,nm(team),String(n)),k*1000));
    setTimeout(end,START_MS);
  }else{
    $('#bjStatus').textContent='Choosing who goes first…';
    // flip durations grow geometrically and sum to exactly START_MS; the last flip shows the winner
    const n=15,g=1.17;let w=0;for(let i=0;i<n;i++)w+=Math.pow(g,i);const a0=START_MS/w;
    const sides=[];for(let i=0;i<n;i++)sides.push((n-1-i)%2===0?team:(team==='L'?'R':'L'));
    let at=0;sides.forEach((s,i)=>{setTimeout(()=>sideShow(s,nm(s),'?'),Math.round(at));at+=a0*Math.pow(g,i)});
    setTimeout(()=>{sideShow(team,nm(team),'');},START_MS-1);
    setTimeout(end,START_MS);
  }
  window.__startT0=t0;
}
function countdownFirst(team){startSeq('manual',team)}
function spinFirst(){startSeq('random',Math.random()<.5?'L':'R')}

"""
t = t[:a] + new_js + t[b:]

# ---- clockDraw must not overwrite the box while the sequence runs ----
old = "function clockDraw(){\n"
assert old in t
t = t.replace(old, "function clockDraw(){\n  if(spinning)return;\n", 1)

# ---- remove overlay markup/css ----
t = t.replace('<div id="toast"></div><div id="cdOverlay"></div>', '<div id="toast"></div>')
i = t.index("#cdOverlay{")
j = t.index("@keyframes cdpop")
j = t.index("\n", j) + 1
t = t[:i] + t[j:]

# ---- big countdown digit inside the box ----
t = t.replace("</style>", """#sideBox.starting .sidesec{font-size:44px;padding-bottom:6px;color:var(--ink)}
#sideBox.starting small{color:var(--amber)}
#sideBox.starting #sideTxt{font-size:34px}
</style>""", 1)
t = t.replace('<small>CURRENT SIDE</small>', '<small id="sideLbl">CURRENT SIDE</small>')
open('lab_template.html', 'w', encoding='utf-8').write(t)

# the label should read STARTING IN... while the sequence runs
t = open('lab_template.html', encoding='utf-8').read()
t = t.replace("const sb=$('#sideBox');sb.className='cbox starting';", "const sb=$('#sideBox');sb.className='cbox starting';$('#sideLbl').textContent='GET READY';")
t = t.replace("$('#sideBox').classList.remove('starting');", "$('#sideBox').classList.remove('starting');$('#sideLbl').textContent='CURRENT SIDE';")
open('lab_template.html', 'w', encoding='utf-8').write(t)

g = open('../Knowledge_Guide.md', encoding='utf-8').read()
g = g.replace("- **Start countdown:** choosing a team manually (button or `L`/`R`) shows a 3-2-1 countdown before the start image appears and the clock starts; Random uses its spinner instead.",
              "- **Start sequence (exactly 3 s):** shown in the CURRENT SIDE box before the start image appears and the clock starts. Manual pick (button or `L`/`R`): 3 - 2 - 1 for the chosen team. Random: LEFT and RIGHT flip with decaying speed and land on the winner at 3.0 s, so both paths have the same tempo.")
open('../Knowledge_Guide.md', 'w', encoding='utf-8').write(g)
print('ok')
