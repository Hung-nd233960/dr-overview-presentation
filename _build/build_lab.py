import base64
t=open('lab_template.html',encoding='utf-8').read()
e=open('engine.js',encoding='utf-8').read()
b=base64.b64encode(open('base768.jpg','rb').read()).decode()
t=t.replace('/*ENGINE*/',e).replace('/*BASE64*/',b)
open('../DR_Lab.html','w',encoding='utf-8').write(t)
print(len(t))
