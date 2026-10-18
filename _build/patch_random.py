# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()


def rep(a, b):
    global t
    assert a in t, a[:60]
    t = t.replace(a, b)


rep('<button id="coinF">Flip a coin</button>', '<button id="coinF">&#127922; Random <kbd>F</kbd></button>')
rep("button kbd{color:var(--ink)}",
    "button kbd{color:var(--ink)}\n.team.spin{border-color:var(--amber);background:#1d3556;box-shadow:0 0 0 5px rgba(242,177,52,.35)}\n.team.win{border-color:var(--green);box-shadow:0 0 0 6px rgba(63,191,107,.4)}")
# guard setFirst while spinning
rep("function setFirst(t){if(S.first||S.over)return;", "let spinning=false;\nfunction setFirst(t){if(spinning||S.first||S.over)return;")
# random spin
rep("$('#coinF').onclick=()=>setFirst(Math.random()<.5?'L':'R');",
    "$('#coinF').onclick=spinFirst;")
rep("let rulesOn=true;",
    """function spinFirst(){
  if(spinning||S.first||S.over)return;
  spinning=true;
  const winner=Math.random()<.5?'L':'R';
  const seq=[];let d=70,tot=0,side=Math.random()<.5?'L':'R';
  while(tot<3500){seq.push([side,d]);tot+=d;d*=1.16;side=side==='L'?'R':'L'}
  if(seq[seq.length-1][0]!==winner)seq.push([winner,d]);
  ['coinL','coinR','coinF'].forEach(i=>$('#'+i).disabled=true);
  $('#bjStatus').textContent='Picking who goes first\\u2026';
  const mark=x=>{$('#tL').classList.toggle('spin',x==='L');$('#tR').classList.toggle('spin',x==='R')};
  (function run(i){
    if(i>=seq.length){
      $('#t'+winner).classList.remove('spin');$('#t'+winner).classList.add('win');
      $('#bjStatus').textContent=(winner==='L'?'Team Left':'Team Right')+' picks first!';
      setTimeout(()=>{['L','R'].forEach(x=>$('#t'+x).classList.remove('win','spin'));['coinL','coinR','coinF'].forEach(i=>$('#'+i).disabled=false);spinning=false;setFirst(winner)},1100);
      return;
    }
    mark(seq[i][0]);setTimeout(()=>run(i+1),seq[i][1]);
  })(0);
}
let rulesOn=true;""")
rep("else if(k==='f'&&!S.first)setFirst(Math.random()<.5?'L':'R');", "else if(k==='f'&&!S.first)spinFirst();")
open('lab_template.html', 'w', encoding='utf-8').write(t)

# docs / notes wording
s = open('script_data.py', encoding='utf-8').read()
s = s.replace("B flips a coin: `Left first` / `Right first`.", "B presses **Random** (a 3\\u20134 second spinner decides who picks first) or clicks a team.")
open('script_data.py', 'w', encoding='utf-8').write(s)
d = open('build_deck.js', encoding='utf-8').read()
d = d.replace("First pick alternates (coin flip in round 1).", "First pick alternates (the Random button decides round 1).")
open('build_deck.js', 'w', encoding='utf-8').write(d)
c = open('../Rehearsal_Checklist.md', encoding='utf-8').read()
c = c.replace("split room, coin flip, 4 rounds", "split room, Random picks the first team, 4 rounds")
open('../Rehearsal_Checklist.md', 'w', encoding='utf-8').write(c)
print('ok')
