I=open(0).read().split();n=int(I[0]) 
def C(g,x,y,ch,v): 
 s=[(x,y)];v.add((x,y));c=[] 
 while s: 
  a,b=s.pop();c+=[(a,b)] 
  for p,q in((a+1,b),(a-1,b),(a,b+1),(a,b-1)): 
   if 0<=p<10 and 0<=q<20 and(p,q)not in v and g[p][q]==ch:v.add((p,q));s+=[(p,q)] 
 return c 
for t in range(n): 
 g=I[1+t*10:11+t*10];v=set();d=0;o=0 
 for i in range(10): 
  for j in range(20): 
   if(i,j)not in v: 
    c=C(g,i,j,g[i][j],v) 
    if g[i][j]=='.':d+=1 
    elif len(c)>5 and all(0<a<9 and 0<b<19 for a,b in c):o=1 
 print((d<2)+2*o)