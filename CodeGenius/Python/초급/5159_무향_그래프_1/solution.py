n,m,*e=map(int,open(0).read().split());g=[[0]*n for _ in range(n)] 
for a,b in zip(e[::2],e[1::2]):g[a-1][b-1]=g[b-1][a-1]=1 
for r in g:print(*r,end=' \n')