t=open('lab_template.html',encoding='utf-8').read()
def rep(a,b):
    global t
    assert a in t,a[:60]; t=t.replace(a,b)
rep("  ['L','R'].forEach(t=>{const T=S.T[t];drawTo($('#c'+t),drImg(T.r,T.seeds[T.seeds.length-1]));\n    const h=$('#h'+t);h.innerHTML='';T.hist.forEach(",
    "  ['L','R'].forEach(t=>{const T=S.T[t];if(S.first)drawTo($('#c'+t),drImg(T.r,T.seeds[T.seeds.length-1]));else hiddenPanel($('#c'+t));\n    const h=$('#h'+t);h.innerHTML='';(S.first?T.hist:[]).forEach(")
rep("function bjRender(){",
    "// the start image stays hidden until the game (and the clock) starts, so nobody gets thinking time for free\n"
    "function hiddenPanel(cv){const x=cv.getContext('2d');x.fillStyle='#0a1322';x.fillRect(0,0,cv.width,cv.height);x.fillStyle='#6f86a6';x.textAlign='center';x.font='bold 44px Calibri,Arial,sans-serif';"
    "x.fillText('Start image hidden',cv.width/2,cv.height/2-14);x.font='36px Calibri,Arial,sans-serif';x.fillText('until the game starts',cv.width/2,cv.height/2+40)}\n"
    "function bjRender(){")
open('lab_template.html','w',encoding='utf-8').write(t)
for p,pairs in (('../Knowledge_Guide.md',None),):
    pass
g=open('../Knowledge_Guide.md',encoding='utf-8').read()
g+="- **Hidden start:** the start image (and each team's history) is hidden until a first team is chosen, which is also when the 3:00 clock starts, so nobody gets free thinking time. The Ideal image stays visible.\n"
open('../Knowledge_Guide.md','w',encoding='utf-8').write(g)
s=open('../Rehearsal_Checklist.md',encoding='utf-8').read()
s=s.replace("## Backup plan","Note: in Blackjack the start image is hidden until Random/a team is chosen (clock starts then); the Ideal image is visible from the start.\n\n## Backup plan",1)
open('../Rehearsal_Checklist.md','w',encoding='utf-8').write(s)
