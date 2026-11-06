n=int(input());P=[[0]*17 for _ in range(17)];P[1][1]=1 
for k in range(2,n+1): 
 Q=[[0]*17 for _ in range(17)] 
 for i in range(1,k+1): 
  for j in range(1,k-i+2):Q[i][j]=P[i][j]+P[i-1][j]+P[i][j-1] 
 P=Q 
for i in range(1,n+1):print(*P[i][1:n-i+2],end=' \n')