// Render simulated images with the SAME engine used in DR_Lab.html -> raw gray files
const fs=require('fs'),E=require('./engine.js');
const {execSync}=require('child_process');
const N=768;
// decode base image through python (PIL) to raw
execSync('python -c "from PIL import Image;open(\'base.raw\',\'wb\').write(Image.open(\'base768.jpg\').convert(\'L\').tobytes())"');
const raw=fs.readFileSync('base.raw');const base=new Float32Array(N*N);for(let i=0;i<N*N;i++)base[i]=raw[i]/255;
fs.mkdirSync('sim',{recursive:true});
const out=(name,g)=>fs.writeFileSync('sim/'+name+'.raw',Buffer.from(g.buffer,g.byteOffset,g.length));
const dr=[[0.12005,'dr_0.12',7],[0.25,'dr_0.25',3],[0.5,'dr_0.5',3],[0.72,'dr_0.72',3],[0.96,'dr_0.96',3],[1,'dr_1',3],[1.08,'dr_1.08',3],[3,'dr_3',3],[4,'dr_4',3],[8,'dr_8',3]];
dr.forEach(([r,n,s])=>out(n,E.renderDR(base,N,r,s)));
[0.25,1,4].forEach(r=>out('film_'+r,E.renderFilm(base,N,r)));
console.log('ok');
[1,0.25,3,0.5].forEach((r,i)=>out('warm_'+(i+1),E.renderDR(base,N,r,100+i)));
