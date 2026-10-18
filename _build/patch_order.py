# -*- coding: utf-8 -*-
import re

# ======================= lab logic =======================
t = open('lab_template.html', encoding='utf-8').read()


def rep(a, b):
    global t
    assert a in t, a[:80]
    t = t.replace(a, b)


rep("function newState(){return{round:1,first:null,order:null,pos:0,usedCard:null,over:false,",
    "// Turn order: first team once, the second team twice in a row (its trade for going second), then alternate.\n"
    "// F = first mover, S = second mover: 4 scans each.\n"
    "const PATTERN='FSSFSFSF';\n"
    "function newState(){return{i:0,first:null,last:{L:null,R:null},prev:null,over:false,")
rep("function curTeam(){if(S.over||!S.first)return null;return S.order[S.pos]}",
    "function other(t){return t==='L'?'R':'L'}\n"
    "function teamAt(k){return PATTERN[k]==='F'?S.first:other(S.first)}\n"
    "function curTeam(){if(S.over||!S.first)return null;return teamAt(S.i)}")
a = t.index("function advance(){")
b = t.index("let spinning=false;")
t = t[:a] + """function advance(){
  // skip entries of teams that have stood / hit the dose limit; end when nobody is active or the order is used up
  for(;;){
    if(S.i>=PATTERN.length||(!active('L')&&!active('R'))){S.over=true;return}
    if(active(teamAt(S.i)))return;
    S.i++;
  }
}
""" + t[b:]
rep("S.first=t;S.order=[t,t==='L'?'R':'L'];S.pos=0;advance();bjRender()}", "S.first=t;S.i=0;advance();bjRender()}")
rep("  if(S.pos===1&&S.usedCard===ci)return; // no copying\n", "  if(S.last[other(t)]===ci)return; // no copying: not the card your opponent played last\n")
rep("T.seeds.push(SEEDg+S.round*10+(t==='L'?1:2));\n  if(S.pos===0)S.usedCard=ci;\n", "T.seeds.push(SEEDg+S.i*10+(t==='L'?1:2));\n  S.last[t]=ci;\n")
rep("STANDS',true)}\n  S.pos++;advance();bjRender();", "STANDS',true)}\n  S.prev=t;S.i++;advance();bjRender();")
rep("function doStand(){const t=curTeam();if(!t||paused)return;snap();S.T[t].stand=true;S.pos++;advance();bjRender()}",
    "function doStand(){const t=curTeam();if(!t||paused)return;snap();S.T[t].stand=true;S.prev=t;S.i++;advance();bjRender()}")
# status + pill + cards
rep("if(!S.first)msg='Who picks first in round 1? Press Random or choose a team';", "if(!S.first)msg='Who plays first? Press Random or choose a team';")
rep("msg='Round '+S.round+' of 4 \\u2014 '+nm(t)+' keeps playing ('", "msg='Turn '+(S.i+1)+' of 8 \\u2014 '+nm(t)+' keeps playing ('")
rep("else msg='Round '+S.round+' of 4 \\u2014 '+nm(t)+' to play'+(S.pos===1?' (second pick)':' (first pick)')}",
    "else msg='Turn '+(S.i+1)+' of 8 \\u2014 '+nm(t)+' to play'+(S.prev===t?' (2nd in a row)':'')}")
rep("'Round '+Math.min(S.round,4)+' / 4'", "'Turn '+Math.min(S.i+1,8)+' / 8'")
rep("(!t||(S.pos===1&&S.usedCard===i))?' used':''", "(!t||S.last[other(t)]===i)?' used':''")
rep("const key=(S.over||!S.first)?'':S.round+'-'+S.pos+'-'+curTeam();", "const key=(S.over||!S.first)?'':S.i+'-'+curTeam();")
rep("snap();S.T[tm].stand=true;S.pos++;advance();", "snap();S.T[tm].stand=true;S.prev=tm;S.i++;advance();")
rep("<span>Who picks first in round 1?</span>", "<span>Who plays first?</span>")

# rules screen text
t = re.sub(r'<div class="rule"><b class="n">3</b><span>.*?</span></div>',
           '<div class="rule"><b class="n">3</b><span><b>Turn order:</b> the first team plays once, the other team then plays <b>twice in a row</b> (its trade for going second), then they alternate: <b>L R R L R L R L</b> (4 scans each).</span></div>', t, count=1, flags=re.S)
t = re.sub(r'<div class="rule"><b class="n">4</b><span>.*?</span></div>',
           '<div class="rule"><b class="n">4</b><span><b>No copying:</b> you cannot play the card your opponent played last. Say <b>STAND</b> when close enough; the other team <b>keeps playing</b>, so standing early gains nothing.</span></div>', t, count=1, flags=re.S)
assert 'L R R L R L R L' in t and 'No copying:</b> you cannot' in t
open('lab_template.html', 'w', encoding='utf-8').write(t)

# ======================= deck =======================
d = open('build_deck.js', encoding='utf-8').read()
n0 = d
d = d.replace("'No copying: the first team’s card is blocked for the second.'", "'Order: first team once, then the other twice in a row, then alternate (L R R L R L R L). No copying: not your opponent’s last card.'")
d = d.replace("'Up to 4 rounds, or STAND (timeout = STAND). Last image counts.'", "'4 scans each, or STAND (timeout = STAND). Last image counts.'")
d = d.replace("'Each round: play a × card. It multiplies your last scan, so cards chain.'", "'Each turn: play a × card. It multiplies your last scan, so cards chain.'")
assert d != n0
d = d.replace("First pick alternates (the Random button decides round 1).", "The Random button decides who plays first; that team plays once, then the other team plays twice in a row (its trade for going second), then they alternate: L R R L R L R L, four scans each.")
d = d.replace("The first team's card is blocked for the second team that round.", "You cannot play the card your opponent played last.")
open('build_deck.js', 'w', encoding='utf-8').write(d)

# ======================= script / checklist =======================
s = open('script_data.py', encoding='utf-8').read()
pairs = [
    ("Each round you play one multiplier card.", "Each turn you play one multiplier card."),
    ("The first team's card is blocked for the second team, so no copying.", "Turn order: the first team plays once, then the other team plays twice in a row, as its trade for going second, and then they alternate. You cannot play the card your opponent played last, so no copying."),
    ("Mỗi vòng, đội chơi một thẻ nhân.", "Mỗi lượt, đội chơi một thẻ nhân."),
    ("Thẻ của đội đi trước bị khóa với đội sau, nên không được chép.", "Thứ tự lượt: đội đi trước chơi một lần, sau đó đội còn lại chơi hai lượt liên tiếp (bù lại vì đi sau), rồi hai đội luân phiên. Không được chơi thẻ mà đối thủ vừa chơi ở lượt gần nhất."),
    ("Up to four rounds, or say STAND", "Up to four scans each, or say STAND"),
    ("Tối đa bốn vòng, hoặc nói STAND", "Tối đa bốn lần chụp mỗi đội, hoặc nói STAND"),
    ("[Run up to 4 rounds within the 3:00 game clock;", "[Run the eight turns (L R R L R L R L if Left plays first) within the 3:00 game clock;"),
    ("After the last round press Reveal", "After the last turn press Reveal"),
    ("[Chơi 4 vòng, mỗi vòng khoảng 25 giây. Đội trưởng gọi thẻ trong 10 giây. Sau vòng cuối bấm Reveal", "[Chơi tám lượt (T P P T P T P T nếu đội Trái đi trước) trong 3:00 đồng hồ chung. Đội trưởng gọi thẻ nhanh. Sau lượt cuối bấm Reveal"),
    ("Each round: the team on turn discusses for at most 10 s;", "Each turn: the team on turn discusses for at most 10 s;"),
    ("keys 1–8 = cards in order", "keys 1–9 = cards in order"),
    ("(the first team’s card is greyed out for the second team), alternates the first pick each round, and announces", "(the card your opponent played last is greyed out), checks the turn order (first team once, other team twice in a row, then alternate), and announces"),
    ("its remaining rounds. P pauses", "its remaining turns. P pauses"),
    ("After round 4, or when both teams", "After the 8th turn, or when both teams"),
]
for a, b in pairs:
    assert a in s, a[:60]
    s = s.replace(a, b)
open('script_data.py', 'w', encoding='utf-8').write(s)

c = open('../Rehearsal_Checklist.md', encoding='utf-8').read()
for a, b in [
    ("(no-copy, alternate first pick, dose-bar colour;", "(no-copy, turn order L R R L R L R L, dose-bar colour;"),
    ("`1`–`8` cards", "`1`–`9` cards"),
    ("4 rounds ≈ 25 s each", "8 turns (first team once, other team twice in a row, then alternate)"),
    ("shorten Blackjack to 3 rounds", "shorten Blackjack to 3 scans each"),
]:
    assert a in c, a
    c = c.replace(a, b)
open('../Rehearsal_Checklist.md', 'w', encoding='utf-8').write(c)

g = open('../Knowledge_Guide.md', encoding='utf-8').read()
g += """
## 18. Turn order and fairness (Blackjack)

- Order: the first team (chosen by Random) plays once, the second team then plays **twice in a row** as compensation for moving second, then they alternate: **L R R L R L R L** if Left plays first (4 scans each). Entries of a team that has stood or hit the dose limit are skipped.
- **No copying:** you cannot play the card your opponent played on their most recent turn.
- Why: going first is treated as a head start on the shared game clock, so the second team gets two consecutive turns in return. The second team also sees the first team's image before choosing; whether that offsets the head start is a design choice to tune in rehearsal (an option is to hide the opponent's latest image until both have played).
"""
open('../Knowledge_Guide.md', 'w', encoding='utf-8').write(g)
print('ok')
