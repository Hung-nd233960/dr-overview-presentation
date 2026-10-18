# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()


def rep(a, b):
    global t
    assert a in t, a[:60]
    t = t.replace(a, b)


# clearer status when the other team has stood / been stopped
rep("else msg='Round '+S.round+' of 4 — '+(t==='L'?'Team Left':'Team Right')+' to play'+(S.pos===1?' (second pick)':' (first pick)');",
    "else{const o=t==='L'?'R':'L',nm=x=>x==='L'?'Team Left':'Team Right';\n"
    "    if(S.T[o].stand||S.T[o].stopped)msg='Round '+S.round+' of 4 \\u2014 '+nm(t)+' keeps playing ('+nm(o)+(S.T[o].stand?' stood':' hit the dose limit')+')';\n"
    "    else msg='Round '+S.round+' of 4 \\u2014 '+nm(t)+' to play'+(S.pos===1?' (second pick)':' (first pick)')}")
# rules text
rep("<span>Up to <b>4 rounds</b>. Say <b>STAND</b> any time you think you are close enough.</span>",
    "<span>Up to <b>4 rounds</b>. Say <b>STAND</b> when you think you are close enough. The other team <b>keeps playing</b> its remaining rounds, so standing early gains nothing.</span>")
open('lab_template.html', 'w', encoding='utf-8').write(t)

# deck notes + slide 11 rule 4
d = open('build_deck.js', encoding='utf-8').read()
d = d.replace("'Up to 4 rounds, or STAND. Your last image counts.'", "'Up to 4 rounds, or STAND. The other team keeps playing. Last image counts.'")
d = d.replace("Up to 4 rounds or STAND. The last image is the submission.", "Up to 4 rounds or STAND; a team that stands is out, but the other team keeps playing all its remaining rounds, so standing early gives no advantage. The last image is the submission.")
open('build_deck.js', 'w', encoding='utf-8').write(d)

s = open('script_data.py', encoding='utf-8').read()
s = s.replace("Up to four rounds, or say STAND if you think you are close enough. Your last image is your submission.",
              "Up to four rounds, or say STAND if you think you are close enough. If one team stands, the other keeps playing its remaining rounds, so standing early gains nothing. Your last image is your submission.")
s = s.replace("Tối đa bốn vòng, hoặc nói STAND nếu thấy đã đủ gần. Ảnh cuối cùng là bài nộp.",
              "Tối đa bốn vòng, hoặc nói STAND nếu thấy đã đủ gần. Nếu một đội dừng, đội kia vẫn chơi tiếp các vòng còn lại, nên dừng sớm không có lợi thế. Ảnh cuối cùng là bài nộp.")
s = s.replace("A mistake? Press U (undo).", "If one team stands, the other keeps playing its remaining rounds. A mistake? Press U (undo).")
open('script_data.py', 'w', encoding='utf-8').write(s)
print('ok', 'keeps playing' in d, 'keeps playing' in s)
