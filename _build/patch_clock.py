# -*- coding: utf-8 -*-
import re

t = open('lab_template.html', encoding='utf-8').read()


def rep(a, b):
    global t
    assert a in t, a[:70]
    t = t.replace(a, b)


# ---------- HTML ----------
rep('<span class="clock" id="tClock"><small>TURN</small>30</span><span class="clock" id="gClock"><small>GAME</small>3:00</span></div>', '</div>')
rep('<div class="grid3">',
    '<div class="grid3">\n'
    '      <div id="gClockBig" class="gclock"><span class="dot"></span>'
    '<svg class="hg" viewBox="0 0 24 24" width="42" height="42"><path d="M6 2h12v4l-5 6 5 6v4H6v-4l5-6-5-6z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M8.5 5h7l-3.5 4.2z" fill="currentColor"/><path d="M8 19h8l-4-4.5z" fill="currentColor"/></svg>'
    '<div><small>GAME CLOCK</small><b id="gTime">3:00</b></div></div>', )
rep('<div class="team" id="tL"><h2>TEAM LEFT</h2>', '<div class="team" id="tL"><div class="tbadge" id="tbL"><span>30</span></div><h2>TEAM LEFT</h2>')
rep('<div class="team" id="tR"><h2>TEAM RIGHT</h2>', '<div class="team" id="tR"><div class="tbadge" id="tbR"><span>30</span></div><h2>TEAM RIGHT</h2>')
t = t.replace('Match this image with as little dose as possible', 'Match this with the least dose')

# ---------- CSS ----------
css = """
/* clocks: big game clock (centre) + turn ring on the playing team */
.grid3{position:relative}
.team{position:relative}
.team.act h2::after{content:''}
.gclock{position:absolute;left:50%;bottom:4px;transform:translateX(-50%);display:flex;align-items:center;gap:14px;background:#0a1322;border:3px solid #2c4468;border-radius:16px;padding:6px 26px 6px 18px;z-index:2;color:var(--teal);box-shadow:0 6px 18px rgba(0,0,0,.45)}
.gclock small{display:block;font-size:12px;font-weight:700;letter-spacing:1.5px;color:var(--mute)}
.gclock b{display:block;font-size:46px;line-height:1;font-variant-numeric:tabular-nums;color:var(--ink)}
.gclock .dot{width:14px;height:14px;border-radius:50%;background:#555;flex:none}
.gclock.run .dot{background:var(--red);animation:tick 1s steps(1) infinite}
@keyframes tick{50%{opacity:.15}}
.gclock .hg{flex:none}
.gclock.run .hg{animation:flip 4s ease-in-out infinite}
@keyframes flip{0%,40%{transform:rotate(0)}50%,90%{transform:rotate(180deg)}100%{transform:rotate(360deg)}}
.gclock.warn{border-color:var(--amber);color:var(--amber)}
.gclock.warn b{color:var(--amber)}
.gclock.crit{border-color:var(--red);color:var(--red)}
.gclock.crit b{color:var(--red);animation:blink .6s infinite}
.tbadge{--p:100;--c:var(--teal);position:absolute;top:4px;right:8px;width:46px;height:46px;border-radius:50%;display:none;align-items:center;justify-content:center;background:conic-gradient(var(--c) calc(var(--p)*1%),#0a1322 0);z-index:2}
.tbadge::before{content:'';position:absolute;inset:5px;border-radius:50%;background:var(--panel)}
.tbadge span{position:relative;font-size:20px;font-weight:800;font-variant-numeric:tabular-nums;color:var(--ink)}
.tbadge.warn{--c:var(--amber)}
.tbadge.warn span{color:var(--amber)}
.tbadge.crit{--c:var(--red)}
.tbadge.crit span{color:var(--red);animation:blink .5s infinite}
.team.act.warn{border-color:var(--amber);box-shadow:0 0 0 4px rgba(242,177,52,.3)}
.team.act.crit{border-color:var(--red);box-shadow:0 0 0 5px rgba(226,87,76,.4)}
"""
rep("</style>", css + "</style>")

# ---------- JS: replace clockDraw ----------
a = t.index("function clockDraw(){")
b = t.index("let toastT=null;")
new = """function clockDraw(){
  const now=paused?pAt:Date.now();
  const live=!!(S&&S.first&&!S.over&&gEnd);
  const gl=live?gEnd-now:(gEnd?Math.max(0,gEnd-now):GLOBAL_MS);
  $('#gTime').textContent=fmt2(gEnd?gEnd-now:GLOBAL_MS);
  $('#gClockBig').className='gclock'+(live&&!paused?' run':'')+(live&&gl<=10000?' crit':live&&gl<=30000?' warn':'');
  const cur=live?curTeam():null;
  ['L','R'].forEach(x=>{
    const b=$('#tb'+x),panel=$('#t'+x),on=!!(cur===x&&tEnd);
    b.style.display=on?'flex':'none';
    panel.classList.remove('warn','crit');
    if(on){
      const rem=tEnd-now;
      b.firstElementChild.textContent=Math.max(0,Math.ceil(rem/1000));
      b.style.setProperty('--p',Math.max(0,Math.min(100,rem/TURN_MS*100)));
      const cls=rem<=5000?'crit':rem<=10000?'warn':'';
      b.className='tbadge'+(cls?' '+cls:'');
      if(cls)panel.classList.add(cls);
    }
  });
}
"""
t = t[:a] + new + t[b:]
open('lab_template.html', 'w', encoding='utf-8').write(t)
print('ok')
