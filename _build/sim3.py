import itertools, math
r0=1/8.33; P=3; LIMIT=50
def Q(r):
    if r<1: return 100*math.sqrt(r)
    if r<=4: return 100.0
    return max(0,100-20*math.log2(r/4))
def run(cards, seq):
    r=r0; D=10*r0; n=0
    for c in seq:
        if D>=LIMIT: break
        r=r0*c; D+=10*r+P; n+=1
    return 2*Q(r)-D, r, Q(r), D, n
for cards in ([2,3,4,6,8,10,15,40],[2,3,4,6,8,10,12,20],[3,4,6,8,10,12,16,24]):
    res=[]
    for n in range(0,5):
        for seq in itertools.product(cards,repeat=n):
            sc,r,q,d,k=run(cards,seq)
            if k==n: res.append((sc,seq,r,q,d))
    res.sort(key=lambda x:-x[0])
    print('CARDS',cards)
    for sc,seq,r,q,d in res[:4]: print(f'  {sc:6.1f} {seq} r={r:.2f} Q={q:.1f} D={d:.1f}')
    singles=[(c,)+run(cards,(c,))[1:4]+(run(cards,(c,))[0],) for c in cards]
    print('  singles:', [(c, round(r,2), round(q,1), round(d,1), round(sc,1)) for c,r,q,d,sc in singles])
