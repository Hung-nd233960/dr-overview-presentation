t=open('lab_template.html',encoding='utf-8').read()
def rep(a,b):
    global t
    assert a in t,a[:60]; t=t.replace(a,b)
rep("function other(t){return t==='L'?'R':'L'}",
    "function other(t){return t==='L'?'R':'L'}\n// no-copy applies only to the turn directly after the opponent's move (not to your own consecutive turn)\nfunction blocked(t,i){const o=other(t);return S.prev===o&&!S.T[o].stand&&S.last[o]===i}")
rep("if(S.last[other(t)]===ci)return; // no copying: not the card your opponent played last","if(blocked(t,ci))return; // no copying: not the card your opponent just played")
rep("(!t||S.last[other(t)]===i)?' used':''","(!t||blocked(t,i))?' used':''")
rep("<b>No copying:</b> you cannot play the card your opponent played last.","<b>No copying:</b> you cannot play the card your opponent just played (your 2nd turn in a row is free).")
open('lab_template.html','w',encoding='utf-8').write(t)
