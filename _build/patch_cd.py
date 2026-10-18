t=open('lab_template.html',encoding='utf-8').read()
def rep(a,b):
    global t
    assert a in t,a[:60]; t=t.replace(a,b)
rep("$('#coinL').onclick=()=>setFirst('L');$('#coinR').onclick=()=>setFirst('R');","$('#coinL').onclick=()=>countdownFirst('L');$('#coinR').onclick=()=>countdownFirst('R');")
rep("else if(k==='l'&&!S.first)setFirst('L');else if(k==='r'&&!S.first)setFirst('R');","else if(k==='l'&&!S.first)countdownFirst('L');else if(k==='r'&&!S.first)countdownFirst('R');")
rep("function spinFirst(){","""// manual pick: 3-2-1 before the game (and the clock) starts
function countdownFirst(team){
  if(spinning||S.first||S.over)return;
  spinning=true;['coinL','coinR','coinF'].forEach(i=>$('#'+i).disabled=true);
  const ov=$('#cdOverlay');ov.style.display='flex';
  const nm=team==='L'?'TEAM LEFT':'TEAM RIGHT';
  let n=3;
  (function tick(){
    if(n===0){ov.style.display='none';['coinL','coinR','coinF'].forEach(i=>$('#'+i).disabled=false);spinning=false;setFirst(team);return}
    ov.innerHTML='<div class="cdwho" style="color:var(--'+(team==='L'?'lc':'rc')+')">'+nm+' goes first</div><div class="cdnum">'+n+'</div>';
    n--;setTimeout(tick,1000);
  })();
}
function spinFirst(){""")
rep('<div id="toast"></div>','<div id="toast"></div><div id="cdOverlay"></div>')
t=t.replace("</style>","""#cdOverlay{position:fixed;inset:0;display:none;flex-direction:column;align-items:center;justify-content:center;background:rgba(8,14,26,.82);z-index:20}
.cdnum{font-size:240px;font-weight:800;line-height:1;color:var(--ink);animation:cdpop 1s ease-out infinite}
.cdwho{font-size:38px;font-weight:800;letter-spacing:2px;margin-bottom:6px}
@keyframes cdpop{0%{transform:scale(1.5);opacity:.2}30%{transform:scale(1);opacity:1}100%{transform:scale(.9);opacity:.9}}
</style>""",1)
open('lab_template.html','w',encoding='utf-8').write(t)
g=open('../Knowledge_Guide.md',encoding='utf-8').read()
g+="- **Start countdown:** choosing a team manually (button or `L`/`R`) shows a 3-2-1 countdown before the start image appears and the clock starts; Random uses its spinner instead.\n"
open('../Knowledge_Guide.md','w',encoding='utf-8').write(g)
