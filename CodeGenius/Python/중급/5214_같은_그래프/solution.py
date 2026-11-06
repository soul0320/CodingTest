I=iter(open(0).read().split());R=lambda:int(next(I)) 
def G(): 
 n,m=R(),R();a=[[0]*n for _ in range(n)] 
 for _ in range(m):u,v=R()-1,R()-1;a[u][v]=a[v][u]=1 
 return n,m,a 
n,m,A=G();k,l,B=G();p=[];u=[0]*k 
def f(i): 
 if i==n:return 1 
 for j in range(k): 
  if not u[j]and sum(A[i])==sum(B[j])and all(A[i][t]==B[j][p[t]]for t in range(i)): 
   u[j]=1;p.append(j) 
   if f(i+1):return 1 
   u[j]=0;p.pop() 
 return 0 
print('YES'if n==k and m==l and f(0)else'NO')