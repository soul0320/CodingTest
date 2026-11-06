w=[input().strip()for _ in range(6)];r=[] 
for i in range(6): 
 for j in range(6): 
  for k in range(6): 
   if len({i,j,k})>2: 
    a=[w[i],w[j],w[k]];c=[''.join(x)for x in zip(*a)];o=[w[t]for t in range(6)if t not in(i,j,k)] 
    if sorted(c)==sorted(o):r+=[a] 
print(*min(r),sep='\n')