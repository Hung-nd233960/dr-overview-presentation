# -*- coding: utf-8 -*-
svg = open('trefoil.svg.txt').read()
t = open('lab_template.html', encoding='utf-8').read()
assert '&#9888; Stronger multiplier' in t
t = t.replace('&#9888; Stronger multiplier', svg + ' Stronger multiplier')
old = "function toast(msg){const e=$('#toast');e.textContent=msg;"
assert old in t
tre = svg.replace('class="trefoil" ', 'class="trefoil" style="vertical-align:-4px;margin-right:8px" ')
t = t.replace(old, "const TREFOIL='" + tre + "';\nfunction toast(msg,icon){const e=$('#toast');e.innerHTML=(icon?TREFOIL:'')+msg.replace(/&/g,'&amp;').replace(/</g,'&lt;');")
a = "toast('\\u26A0 Dose limit reached: '"
assert a in t, 'prefix'
t = t.replace(a, "toast('Dose limit reached: '")
b = "+' STANDS')}"
assert b in t, 'suffix'
t = t.replace(b, "+' STANDS',true)}")
t = t.replace("</style>", ".trefoil{vertical-align:-5px;margin-right:6px;flex:none}\n</style>", 1)
open('lab_template.html', 'w', encoding='utf-8').write(t)
print('ok')
