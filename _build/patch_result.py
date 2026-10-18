# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()

a = t.index("  let h='<div class=\"rv\">';")
b = t.index("  $('#bjGame').style.display='none';$('#rvBack')")
new_js = r"""  let h='<div class="rv">';
  const sg=x=>(x>=0?'+':'−')+Math.abs(x).toFixed(1);
  ['L','R'].forEach(t=>{const T=S.T[t],w=win===t;
    h+='<div class="rvteam'+(w?' winner':'')+'">'
      +'<h2 style="color:var(--'+(t==='L'?'lc':'rc')+')">'+(t==='L'?'TEAM LEFT':'TEAM RIGHT')+(w?'<span class="wintag">★ WINNER</span>':'')+'</h2>'
      +'<div class="rvrow"><canvas id="rf'+t+'" width="768" height="768"></canvas><div class="rvinfo"><div class="slabel">SCORE</div>'
      +'<div class="score'+(w?' win':'')+'">'+sc[t].score.toFixed(1)+'</div>'
      +'<div class="eq">Quality <b>'+sc[t].Q.toFixed(1)+'</b> × 2 − Dose <b>'+sc[t].D.toFixed(1)+'</b></div>'
      +'<div class="note">Submitted image: '+(T.r*100).toFixed(0)+'% of ideal exposure<br>DI '+sg(E.di(T.r))+'</div></div></div>'
      +'<div class="imgs" id="ri'+t+'"></div></div>'});
  h+='</div><div class="punch">They can look the same. Only the <b>Deviation Index (DI)</b> shows who gave more exposure. DI +3 &asymp; 2&times; the exposure.</div><div class="btns" style="margin-top:10px"><button class="sec" id="rvBack">&#9664; Back to game</button><button id="rvNew">New game</button></div>';
  const rb=$('#revealbox');rb.innerHTML=h;rb.style.display='block';
  ['L','R'].forEach(t=>{const T=S.T[t],box=$('#ri'+t),n=T.hist.length-1;
    drawTo($('#rf'+t),drImg(T.hist[n],T.seeds[n]));
    T.hist.forEach((r,i)=>{const d=document.createElement('div');d.className='im'+(i===n?' last':'');const c=mk(200,200);drawTo(c,drImg(r,T.seeds[i]));d.appendChild(c);
      const l1=document.createElement('div');l1.className='l1';l1.textContent=T.cards[i];d.appendChild(l1);
      const l2=document.createElement('div');l2.className='l2';l2.textContent=(r*100).toFixed(0)+'% · DI '+sg(E.di(r));d.appendChild(l2);box.appendChild(d)})});
"""
t = t[:a] + new_js + t[b:]

css = """
/* larger results page */
#revealbox{padding:4px 8px}
.rv{gap:18px;align-items:stretch}
.rvteam{width:612px;padding:12px 14px 14px;border:3px solid #223a5a;border-radius:16px;text-align:center}
.rvteam.winner{border-color:var(--amber);box-shadow:0 0 0 4px rgba(242,177,52,.25)}
.rvteam h2{margin:0 0 8px;font-size:28px;letter-spacing:.5px}
.wintag{color:var(--amber);font-size:20px;margin-left:14px}
.rvrow{display:flex;gap:20px;align-items:center;justify-content:center}
.rvrow canvas{width:256px;height:256px;border-radius:8px;box-shadow:0 4px 18px rgba(0,0,0,.45);flex:none}
.rvinfo{text-align:left}
.slabel{font-size:14px;letter-spacing:2.5px;color:var(--mute);font-weight:700}
.score{font-size:72px;line-height:1;font-weight:800}
.eq{font-size:20px;margin-top:10px}
.rvinfo .note{font-size:17px;color:var(--mute);margin-top:10px;line-height:1.35}
.rvteam .imgs{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:12px;justify-content:center}
.rvteam .im{text-align:center}
.rvteam .im canvas{width:100%;height:auto;aspect-ratio:1/1;border-radius:6px;border:2px solid #2c4468}
.rvteam .im.last canvas{border-color:var(--teal)}
.rvteam .im .l1{font-size:16px;font-weight:800;margin-top:2px}
.rvteam .im .l2{font-size:12px;color:var(--mute);white-space:nowrap}
.punch{font-size:24px;margin-top:12px}
"""
t = t.replace("</style>", css + "</style>", 1)
open('lab_template.html', 'w', encoding='utf-8').write(t)
print('ok')
