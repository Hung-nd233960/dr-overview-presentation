import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
NAVY='#14325C'; TEAL='#1FB5A8'; AMB='#F2B134'; RED='#E2574C'; GRN='#3FBF6B'; INK='#1B2B3A'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'axes.edgecolor':INK,'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK})

# 1) H&D curve (idealised, Seeram Fig 1.4 values)
x=np.linspace(0,10,400)
od=0.15+3.2/(1+np.exp(-(x-5)*0.95))
fig,ax=plt.subplots(figsize=(7.2,5.0),dpi=200)
ax.plot(x,od,color=NAVY,lw=4)
ax.axhspan(0,0.2,color=AMB,alpha=.35); 
ax.axhspan(0.3,2.2,color=GRN,alpha=.18); ax.axhspan(3.0,3.5,color=RED,alpha=.25)
ax.text(5.6,0.3,'TOE (underexposed)\nOD ~0.12-0.20: light',fontsize=12,color=INK)
ax.text(6.5,1.0,'STRAIGHT LINE (slope)\nuseful range\nOD ~0.3-2.2',fontsize=12,color=INK)
ax.text(0.2,3.05,'SHOULDER: overexposed\nOD ~3.2 (black)',fontsize=12,color=INK)
ax.set_xlabel('Log relative exposure'); ax.set_ylabel('Optical density (OD)')
ax.set_xticks([]); ax.set_ylim(0,3.6); ax.set_xlim(0,10)
for s in ['top','right']: ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig('fig/hd_curve.png',transparent=False,facecolor='white'); plt.close()

# 2) response curves: film (S) vs digital (linear) vs log-exposure -> relative output
fig,axs=plt.subplots(1,2,figsize=(9.6,4.3),dpi=200)
e=np.linspace(-2,2,400)  # log10 exposure
film=1/(1+np.exp(-4.0*e)); 
ax=axs[0]; ax.plot(e,film,color=NAVY,lw=4)
ax.axvspan(-0.35,0.35,color=GRN,alpha=.25); ax.text(0,0.06,'useful\nrange',ha='center',fontsize=13)
ax.set_title('Film: S-curve (narrow latitude)',fontsize=15,color=NAVY)
ax.set_xlabel('Log exposure'); ax.set_ylabel('Relative output (darkness)'); ax.set_xticks([]); ax.set_yticks([])
ax=axs[1]; lin=np.linspace(0,1,100); ax.plot(lin,lin,color=TEAL,lw=4)
ax.axvspan(0.03,0.97,color=GRN,alpha=.25); ax.text(0.5,0.08,'useful range: very wide',ha='center',fontsize=13)
ax.set_title('Digital detector: linear (wide latitude)',fontsize=15,color=TEAL)
ax.set_xlabel('Exposure (linear)'); ax.set_ylabel('Detector signal'); ax.set_xticks([]); ax.set_yticks([])
for a in axs:
    for s in ['top','right']: a.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig('fig/response.png',facecolor='white'); plt.close()

# 3) DI scale bar
fig,ax=plt.subplots(figsize=(8.4,1.7),dpi=200)
segs=[(-9,-2,RED),(-2,2,GRN),(2,3,AMB),(3,9,RED)]
for a,b,c in segs: ax.barh(0,b-a,left=a,color=c,height=.6)
ax.set_xlim(-9,9); ax.set_ylim(-.6,.9); ax.set_yticks([]); ax.set_xticks([-9,-6,-3,0,3,6,9]); ax.set_xticklabels(['-9','-6','-3','0','+3','+6','+9'],fontsize=15)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.text(-5.5,0.0,'<= -2: check noise',ha='center',va='center',fontsize=12,color='white',weight='bold')
ax.text(0,0.0,'target -2 to +2',ha='center',va='center',fontsize=12,color=INK,weight='bold')
ax.text(6,0.0,'>= +3: consult radiologist',ha='center',va='center',fontsize=12,color='white',weight='bold')
fig.tight_layout(); fig.savefig('fig/di_scale.png',facecolor='white'); plt.close()

# 4) image sets
def L(n): return Image.open(f'sim/{n}.png')
def save(n,name,size=700):
    L(n).resize((size,size),Image.LANCZOS).save(f'fig/{name}.png')
save('film_4','film_4x'); save('dr_4','dr_4x'); save('film_0.25','film_q'); save('film_1','film_1x')
save('dr_0.12','start'); save('dr_1','ideal'); save('dr_3','dr_3x')
# warm-up montage 1..4 = 1x, .25, 3x, .5 (same seeds as lab: 100+i, regenerate via node)
