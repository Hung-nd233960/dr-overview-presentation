# -*- coding: utf-8 -*-
t = open('lab_template.html', encoding='utf-8').read()

lines = t.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('    <div id="coinbar">')]
assert len(idx) == 1, idx
block = lines.pop(idx[0])
assert 'id="coinF"' in block and 'id="coinR"' in block and 'id="coinL"' in block
t = '\n'.join(lines)

# put it first inside the playbar (shown instead of the cards until a first team is chosen)
a = '    <div class="playbar">\n'
assert a in t
t = t.replace(a, a + block + '\n', 1)

old = "$('#coinbar').style.display=S.first?'none':'flex';"
assert old in t
t = t.replace(old, old + "document.querySelector('.cardcol').style.display=S.first?'':'none';")
old_css = "#coinbar{display:none;justify-content:center;align-items:center;gap:14px;margin:16px 0 4px;font-size:21px}"
assert old_css in t
t = t.replace(old_css, "#coinbar{display:none;justify-content:center;align-items:center;gap:14px;margin:0;font-size:21px;min-height:116px}")
open('lab_template.html', 'w', encoding='utf-8').write(t)
print('ok')
