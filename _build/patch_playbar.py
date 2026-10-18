# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()


def rep(a, b):
    global t
    assert a in t, a[:70]
    t = t.replace(a, b)


note = '    <div id="cardnote">Each card multiplies your <b>last</b> scan, so cards chain (&times;6 then &times;3 = &times;18 of the start)</div>\n'
rep(note, '')
rep('<div id="toast"></div>\n    <div class="grid3">', '<div id="toast"></div>\n' + note + '    <div class="grid3">')
rep('    <div id="cards"></div>\n    <div class="btns">', '    <div class="playbar">\n    <div id="cards"></div>\n    <div class="ctrls">')
rep('<button class="sec" id="newgame">New game <kbd>N</kbd></button>\n    </div>\n  </div>',
    '<button class="sec" id="newgame">New game <kbd>N</kbd></button>\n    </div>\n    </div>\n  </div>')
t = t.replace('width:196px;height:196px', 'width:172px;height:172px')
rep("b.textContent=l;b.onclick=()=>playCard(i);", "b.textContent=l;b.setAttribute('data-l',l);b.onclick=()=>playCard(i);")

css = """
/* playing-card styled multipliers + control cluster */
.statusbar{margin-bottom:6px}
#cardnote{text-align:center;font-size:17px;color:var(--mute);margin:0 0 12px}
.playbar{display:flex;gap:30px;justify-content:center;align-items:center;margin-top:12px}
#cards{display:flex;gap:10px;margin:0}
.card{position:relative;display:flex;align-items:center;justify-content:center;width:82px;height:116px;padding:0;border-radius:12px;background:#fbfcfe;color:#12304a;border:2px solid #cfd9e6;font-size:36px;font-weight:800;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,.4);transition:transform .12s,box-shadow .12s}
.card::before,.card::after{content:attr(data-l);position:absolute;font-size:15px;font-weight:800;line-height:1}
.card::before{top:7px;left:8px}
.card::after{bottom:7px;right:8px;transform:rotate(180deg)}
.card:hover:not(.used){transform:translateY(-6px);box-shadow:0 10px 20px rgba(0,0,0,.5);border-color:var(--teal)}
.card.used{background:#3a4658;color:#6c7a90;border-color:#3a4658;text-decoration:line-through;cursor:not-allowed;box-shadow:none}
.ctrls{display:grid;grid-template-columns:repeat(3,auto);gap:8px}
.ctrls button{font-size:17px;padding:8px 14px;white-space:nowrap}
"""
rep("</style>", css + "</style>")
open('lab_template.html', 'w', encoding='utf-8').write(t)
print('ok')
