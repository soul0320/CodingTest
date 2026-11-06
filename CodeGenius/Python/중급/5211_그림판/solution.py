n,m=map(int,input().split());g=[input().strip()for _ in range(n)];v=[[0]*m for _ in g];R=Bl=0 
for i in range(n): 
 for j in range(m): 
  if g[i][j]!='X'and not v[i][j]: 
   v[i][j]=1;s=[(i,j)];a=b=0 
   while s: 
    x,y=s.pop();c=g[x][y];a+=c=='A';b+=c=='B' 
    for p,q in((x+1,y),(x-1,y),(x,y+1),(x,y-1)): 
     if 0<=p<n and 0<=q<m and not v[p][q]and g[p][q]!='X':v[p][q]=1;s+=[(p,q)] 
   if a>b:R+=a 
   else:Bl+=b 
print(R,Bl)