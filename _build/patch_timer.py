# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()


def rep(a, b):
    global t
    assert a in t, a[:70]
    t = t.replace(a, b)


# ---------- CSS ----------
rep("button kbd{color:var(--ink)}",
    "button kbd{color:var(--ink)}\n"
    ".clock{font-variant-numeric:tabular-nums;font-weight:800;font-size:22px;border-radius:10px;padding:3px 14px;background:#0a1322;border:2px solid #2c4468;white-space:nowrap;color:var(--ink)}\n"
    ".clock small{font-size:12px;font-weight:600;color:var(--mute);margin-right:6px;letter-spacing:.5px}\n"
    ".clock.warn{color:var(--amber);border-color:var(--amber)}\n"
    ".clock.crit{color:#fff;background:var(--red);border-color:var(--red);animation:blink .6s infinite}\n"
    "@keyframes blink{50%{opacity:.55}}\n"
    "#toast{position:fixed;left:50%;top:78px;transform:translateX(-50%);background:var(--red);color:#fff;font-size:26px;font-weight:800;padding:12px 30px;border-radius:14px;box-shadow:0 8px 30px rgba(0,0,0,.5);display:none;z-index:9}")

# ---------- HTML ----------
rep('<span class="pill" id="roundPill">Round 1 / 4</span><div class="status" id="bjStatus"></div></div>',
    '<span class="pill" id="roundPill">Round 1 / 4</span><div class="status" id="bjStatus"></div><span class="clock" id="tClock"><small>TURN</small>30</span><span class="clock" id="gClock"><small>GAME</small>3:00</span></div><div id="toast"></div>')
rep('<button class="sec" id="rulesBtn">Rules</button>',
    '<button class="sec" id="pauseBtn">Pause <kbd>P</kbd></button><button class="sec" id="rulesBtn">Rules</button>')
rep('<div class="rule"><b class="n">5</b><span>Your <b>last image</b> is your submission, not your best one.</span></div>',
    '<div class="rule"><b class="n">5</b><span>Your <b>last image</b> is your submission, not your best one.</span></div>\n'
    '        <div class="rule"><b class="n">6</b><span><b>Clocks:</b> 30 s per turn and 3:00 for the whole game. If your turn clock runs out, your team <b>STANDS</b> at once. When the game clock ends, <b>both teams STAND</b>.</span></div>')

# ---------- JS ----------
rep("function setFirst(t){if(spinning||S.first||S.over)return;snap();S.first=t;",
    "function setFirst(t){if(spinning||S.first||S.over)return;snap();gEnd=Date.now()+GLOBAL_MS;S.first=t;")
rep("function playCard(ci){\n  const t=curTeam();if(!t)return;", "function playCard(ci){\n  const t=curTeam();if(!t||paused)return;")
rep("function doStand(){const t=curTeam();if(!t)return;", "function doStand(){const t=curTeam();if(!t||paused)return;")
rep("function bjNew(){S=newState();stack=[];hideReveal();", "function bjNew(){S=newState();stack=[];clocksReset();hideReveal();")
rep("function bjUndo(){if(!stack.length)return;S=JSON.parse(stack.pop());hideReveal();bjRender()}",
    "function bjUndo(){if(!stack.length)return;S=JSON.parse(stack.pop());hideReveal();turnKey='';if(gEnd&&gEnd<Date.now()+30000)gEnd=Date.now()+30000;bjRender()}")
rep("$('#bjStatus').textContent=msg;", "$('#bjStatus').textContent=paused?'\\u23F8 Paused \\u2014 press P to resume':msg;")
rep("$('#reveal').disabled=!S.over;$('#reveal').classList.toggle('ready',S.over);",
    "$('#reveal').disabled=!S.over;$('#reveal').classList.toggle('ready',S.over);clockSync();")

clock = """
// ---------- clocks: 30 s per turn (timeout = STAND), 3:00 for the whole game (end = both STAND) ----------
const _q=new URLSearchParams(location.search);const TURN_MS=(+_q.get('turn')||30)*1000,GLOBAL_MS=(+_q.get('game')||180)*1000; /* ?turn= and ?game= (seconds) are for testing */
let gEnd=null,tEnd=null,paused=false,pAt=0,turnKey='';
function clocksReset(){gEnd=null;tEnd=null;paused=false;turnKey='';$('#pauseBtn').innerHTML='Pause <kbd>P</kbd>';clockDraw()}
function clockSync(){
  const key=(S.over||!S.first)?'':S.round+'-'+S.pos+'-'+curTeam();
  if(key!==turnKey){turnKey=key;tEnd=key?Date.now()+TURN_MS:null;if(paused&&tEnd)tEnd+=0}
  clockDraw();
}
function fmt2(ms){const s=Math.max(0,Math.ceil(ms/1000));return Math.floor(s/60)+':'+String(s%60).padStart(2,'0')}
function clockDraw(){
  const now=paused?pAt:Date.now();
  const g=$('#gClock'),tc=$('#tClock');
  const live=S&&S.first&&!S.over&&gEnd;
  g.innerHTML='<small>GAME</small>'+(gEnd?fmt2(gEnd-now):'3:00');
  tc.innerHTML='<small>TURN</small>'+(live&&tEnd?Math.max(0,Math.ceil((tEnd-now)/1000)):'30');
  const gl=live?gEnd-now:1e9,tl=live&&tEnd?tEnd-now:1e9;
  g.className='clock'+(gl<=10000?' crit':gl<=30000?' warn':'');
  tc.className='clock'+(tl<=5000?' crit':tl<=10000?' warn':'');
}
let toastT=null;
function toast(msg){const e=$('#toast');e.textContent=msg;e.style.display='block';clearTimeout(toastT);toastT=setTimeout(()=>e.style.display='none',3500)}
function togglePause(){
  if(!S.first||S.over)return;
  if(!paused){paused=true;pAt=Date.now();$('#pauseBtn').innerHTML='Resume <kbd>P</kbd>'}
  else{const d=Date.now()-pAt;gEnd+=d;if(tEnd)tEnd+=d;paused=false;$('#pauseBtn').innerHTML='Pause <kbd>P</kbd>'}
  bjRender();
}
$('#pauseBtn').onclick=togglePause;
setInterval(()=>{
  if(!S||!S.first||S.over||paused||rulesOn){if(S&&!rulesOn)clockDraw();return}
  const now=Date.now();
  if(gEnd&&now>=gEnd){
    snap();S.T.L.stand=true;S.T.R.stand=true;S.over=true;
    toast('\\u23F1 Game clock ended: both teams STAND');bjRender();return;
  }
  if(tEnd&&now>=tEnd){
    const tm=curTeam();if(!tm){return}
    snap();S.T[tm].stand=true;S.pos++;advance();
    toast('\\u23F1 Time\\u2019s up: '+(tm==='L'?'Team Left':'Team Right')+' STANDS');bjRender();return;
  }
  clockDraw();
},100);
"""
rep("let rulesOn=true;", clock + "let rulesOn=true;")
rep("else if(k==='u')bjUndo();", "else if(k==='u')bjUndo();else if(k==='p')togglePause();")

open('lab_template.html', 'w', encoding='utf-8').write(t)

# docs / deck / checklist
s = open('script_data.py', encoding='utf-8').read()
s = s.replace('("Activity 2: X-ray Blackjack", "D", "2:30"', '("Activity 2: X-ray Blackjack", "D", "3:20"')
s = s.replace('(11, "Activity 2: X-ray Blackjack", "D", "2:30"', '(11, "Activity 2: X-ray Blackjack", "D", "3:20"')
s = s.replace("Your last image is your submission. Score is quality times two",
              "Two clocks run: thirty seconds per turn, and three minutes for the whole game. If your turn clock runs out your team stands at once; when the game clock ends, both teams stand. Your last image is your submission. Score is quality times two")
s = s.replace("Hai đội phải", "Hai đội phải")
s = s.replace("Ảnh cuối cùng là bài nộp. Điểm bằng chất lượng nhân hai trừ liều.",
              "Có hai đồng hồ: ba mươi giây mỗi lượt và ba phút cho cả trò chơi. Hết giờ lượt thì đội đó dừng ngay; hết giờ chung thì cả hai đội dừng. Ảnh cuối cùng là bài nộp. Điểm bằng chất lượng nhân hai trừ liều.")
s = s.replace("[Run 4 rounds, about 25 seconds each. Captain calls the card within 10 seconds.", "[Run up to 4 rounds within the 3:00 game clock; each turn has a 30 s clock (timeout = STAND). Captains call cards quickly.")
s = s.replace("A mistake? Press U (undo).", "P pauses both clocks. A mistake? Press U (undo).")
open('script_data.py', 'w', encoding='utf-8').write(s)
print('time label in data:', '"3:20"' in s)

d = open('build_deck.js', encoding='utf-8').read()
d = d.replace("'ACTIVITY 2  \\u00B7  2.5 min'", "'ACTIVITY 2  \\u00B7  3 min'")
d = d.replace("  const rules = ['Both teams start from the same grainy image.'", "  box(s, 3.35, 1.3, 3.15, 0.55, '30 s per turn \\u00B7 3:00 total', { fill: PALE, size: 16, bold: true, color: NAVY });\n  const rules = ['Both teams start from the same grainy image.'")
d = d.replace("'Up to 4 rounds, or STAND. The other team keeps playing. Last image counts.'", "'Up to 4 rounds, or STAND (timeout = STAND). Last image counts.'")
d = d.replace("Up to 4 rounds or STAND; a team that stands is out", "Clocks: 30 seconds per turn (timeout means that team stands) and 3 minutes for the whole game (when it ends both teams stand). Up to 4 rounds or STAND; a team that stands is out")
open('build_deck.js', 'w', encoding='utf-8').write(d)

c = open('../Rehearsal_Checklist.md', encoding='utf-8').read()
c = c.replace("| 11 | **Activity 2**: X-ray Blackjack | D (A clicks, B referees, C votes) | 2:30 | 13:15 |", "| 11 | **Activity 2**: X-ray Blackjack (20 s rules + 3:00 game clock) | D (A clicks, B referees, C votes) | 3:20 | 14:05 |")
for old, new in [("| 12 | EI, DI and dose creep | D | 1:00 | 14:15 |", "| 12 | EI, DI and dose creep | D | 1:00 | 15:05 |"), ("| 13 | Fluoroscopy and mammography | A | 0:50 | 15:05 |", "| 13 | Fluoroscopy and mammography | A | 0:50 | 15:55 |"), ("| 14 | PACS | B | 1:00 | 16:05 |", "| 14 | PACS | B | 1:00 | 16:55 |"), ("| 15 | QA + take-home | D | 0:45 | 16:50 |", "| 15 | QA + take-home | D | 0:45 | 17:40 |"), ("| Refs | References and AI declaration | D | 0:10 | 17:00 |", "| Refs | References and AI declaration | D | 0:10 | 17:50 |")]:
    assert old in c, old
    c = c.replace(old, new)
c = c.replace("## Timing table (target 17:00)", "## Timing table (target 17:50; the course limit is 18:00)")
c = c.replace("If over time: cut slide 13 to 30 s and slide 5 to 30 s. Course limit is 18 min.", "The Blackjack clocks (30 s per turn, 3:00 for the game) take the segment to about 3:20. That leaves only 10 s of slack: if you run long, cut slide 13 to 30 s and slide 5 to 30 s (saves 35 s).")
open('../Rehearsal_Checklist.md', 'w', encoding='utf-8').write(c)
print('done')
