n,m=map(int,input().split());g=[input().strip()for _ in range(n)] 
for k in range(min(n,m),0,-1): 
 a,b=n//k,m//k 
 if n%k+m%k<1 and all(g[i][j]==g[i%a][j%b]for i in range(n)for j in range(m)):break 
for r in g[:a]:print(r[:b])