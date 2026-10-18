# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()


def rep(a, b):
    global t
    assert a in t, a[:70]
    t = t.replace(a, b)


rep("<span>Who plays first?</span>",
    '<div class="cbtext"><b>Who plays first?</b><span>The team going second gets <b>2 turns in a row</b> to compensate.</span></div>')
rep("</style>",
    ".cbtext{display:flex;flex-direction:column;align-items:flex-start;text-align:left;line-height:1.25;margin-right:6px}\n"
    ".cbtext b{font-size:21px;color:var(--ink)}\n"
    ".cbtext span{font-size:16px;color:var(--amber)}\n"
    ".cbtext span b{font-size:16px;color:var(--amber)}\n"
    "</style>")
# test helper: ?skip=1 opens the game view without picking a first team
rep("const pl=p.get('plays');", "if(p.get('skip'))showRules(false);\n  const pl=p.get('plays');")
open('lab_template.html', 'w', encoding='utf-8').write(t)
print('ok')
