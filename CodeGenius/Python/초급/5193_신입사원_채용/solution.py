n=int(input());p=[tuple(map(int,input().split()))for _ in range(n)];R=range(n) 
d=lambda a,b:a[0]>=b[0]and a[1]>=b[1]and a!=b 
r=list(R) 
def f(x): 
 while r[x]-x:x=r[x] 
 return x 
for i in R: 
 for j in R: 
  if not(d(p[i],p[j])or d(p[j],p[i])):r[f(i)]=f(j) 
c=[f(i)for i in R];g=[[0]*n for _ in R] 
for i in R: 
 for j in R: 
  if c[i]-c[j]and d(p[i],p[j]):g[c[i]][c[j]]=1 
for k in R: 
 for a in R: 
  for b in R: 
   if g[a][k]&g[k][b]:g[a][b]=1 
print(*[1+sum(g[c[j]][c[i]]for j in R)for i in R])