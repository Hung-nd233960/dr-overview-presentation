# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()


def rep(a, b):
    global t
    assert a in t, a[:70]
    t = t.replace(a, b)


# ---------- HTML: two equal boxes side by side ----------
a = t.index('<div id="gClockBig" class="gclock">')
endmark = '<b id="gTime">3:00</b></div></div>'
b = t.index(endmark, a) + len(endmark)
HG = ('<svg class="hg" viewBox="0 0 24 24" width="30" height="30"><path d="M6 2h12v4l-5 6 5 6v4H6v-4l5-6-5-6z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>'
      '<path d="M8.5 5h7l-3.5 4.2z" fill="currentColor"/><path d="M8 19h8l-4-4.5z" fill="currentColor"/></svg>')
new = ('<div class="clockrow">'
       '<div id="gClockBig" class="cbox gclock"><span class="dot"></span>' + HG + '<div class="cmain"><small>TIME LEFT</small><b id="gTime">3:00</b></div></div>'
       '<div id="sideBox" class="cbox" data-side=""><div class="cmain"><small>CURRENT SIDE</small><b id="sideTxt">&ndash;</b></div><div class="sidesec" id="sideSec"></div><i class="sidebar" id="sideBar"></i></div>'
       '</div>')
t = t[:a] + new + t[b:]
rep('<div class="tbadge" id="tbL"><span>30</span></div>', '')
rep('<div class="tbadge" id="tbR"><span>30</span></div>', '')

# ---------- CSS ----------
css = """
/* clock row: TIME LEFT + CURRENT SIDE, equal boxes side by side (no corner rings) */
:root{--lc:#4aa3ff;--rc:#ff8a3d}
.clockrow{position:absolute;left:50%;bottom:2px;transform:translateX(-50%);display:flex;gap:10px;z-index:2}
.cbox,.clockrow .gclock{position:relative;left:auto;bottom:auto;transform:none;width:208px;height:70px;display:flex;align-items:center;gap:10px;padding:0 14px;background:#0a1322;border:2px solid #2c4468;border-radius:14px;box-shadow:0 6px 18px rgba(0,0,0,.45);overflow:hidden;color:var(--teal)}
.cbox .cmain{display:flex;flex-direction:column;min-width:0}
.cbox small{display:block;font-size:11px;font-weight:700;letter-spacing:1.4px;color:var(--mute);white-space:nowrap}
.cbox b{display:block;font-size:38px;line-height:1.05;font-weight:800;color:var(--ink);font-variant-numeric:tabular-nums;white-space:nowrap}
.clockrow .gclock .hg{width:30px;height:30px}
#sideBox[data-side=L] #sideTxt{color:var(--lc)}
#sideBox[data-side=R] #sideTxt{color:var(--rc)}
#sideBox[data-side=L]{border-color:var(--lc)}
#sideBox[data-side=R]{border-color:var(--rc)}
.sidesec{margin-left:auto;font-size:22px;font-weight:800;font-variant-numeric:tabular-nums;color:var(--ink);align-self:flex-end;padding-bottom:9px}
.sidebar{position:absolute;left:0;bottom:0;height:5px;width:0;background:var(--ink);transition:width .1s linear}
#sideBox[data-side=L] .sidebar{background:var(--lc)}
#sideBox[data-side=R] .sidebar{background:var(--rc)}
#sideBox.warn{border-color:var(--amber)}
#sideBox.warn .sidesec{color:var(--amber)}
#sideBox.warn .sidebar{background:var(--amber)}
#sideBox.crit{border-color:var(--red)}
#sideBox.crit .sidesec{color:var(--red);animation:blink .5s infinite}
#sideBox.crit .sidebar{background:var(--red)}
.cbox.gclock.warn{border-color:var(--amber);color:var(--amber)}
.cbox.gclock.crit{border-color:var(--red);color:var(--red)}
/* team colours tie the panels to the CURRENT SIDE box */
#tL h2{color:var(--lc)}
#tR h2{color:var(--rc)}
#tL.act:not(.warn):not(.crit){border-color:var(--lc);box-shadow:0 0 0 4px rgba(74,163,255,.25)}
#tR.act:not(.warn):not(.crit){border-color:var(--rc);box-shadow:0 0 0 4px rgba(255,138,61,.25)}
"""
rep("</style>", css + "</style>")

# ---------- JS: new clockDraw ----------
a = t.index("function clockDraw(){")
b = t.index("let toastT=null;")
new_js = """function clockDraw(){
  const now=paused?pAt:Date.now();
  const live=!!(S&&S.first&&!S.over&&gEnd);
  const gl=live?gEnd-now:(gEnd?Math.max(0,gEnd-now):GLOBAL_MS);
  $('#gTime').textContent=fmt2(gEnd?gEnd-now:GLOBAL_MS);
  $('#gClockBig').className='cbox gclock'+(live&&!paused?' run':'')+(live&&gl<=10000?' crit':live&&gl<=30000?' warn':'');
  const cur=live?curTeam():null;
  const sb=$('#sideBox'),tx=$('#sideTxt'),sec=$('#sideSec'),bar=$('#sideBar');
  ['L','R'].forEach(x=>$('#t'+x).classList.remove('warn','crit'));
  sb.classList.remove('warn','crit');
  if(cur&&tEnd){
    const rem=Math.max(0,tEnd-now);
    sb.dataset.side=cur;tx.textContent=cur==='L'?'LEFT':'RIGHT';
    sec.textContent=Math.ceil(rem/1000)+'s';
    bar.style.width=Math.min(100,rem/TURN_MS*100)+'%';
    const cls=rem<=5000?'crit':rem<=10000?'warn':'';
    if(cls){sb.classList.add(cls);$('#t'+cur).classList.add(cls)}
  }else{
    sb.dataset.side='';tx.textContent=(S&&S.over)?'DONE':'\\u2013';sec.textContent='';bar.style.width='0';
  }
}
"""
t = t[:a] + new_js + t[b:]
open('lab_template.html', 'w', encoding='utf-8').write(t)

c = open('../Rehearsal_Checklist.md', encoding='utf-8').read()
old_start = c.index("- [ ] Blackjack clocks:")
old_end = c.index("\n", old_start)
c = c[:old_start] + "- [ ] Blackjack clocks: two equal boxes under the START/Ideal panels. TIME LEFT = the 3:00 game clock (hourglass flips, red dot blinks; yellow at 30 s, red at 10 s). CURRENT SIDE = LEFT (blue) or RIGHT (orange) with that team's 30 s turn countdown and a draining bar (yellow at 10 s, red at 5 s). `P` pauses both." + c[old_end:]
open('../Rehearsal_Checklist.md', 'w', encoding='utf-8').write(c)
print('ok')
