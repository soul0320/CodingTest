n,k,*a=map(int,open(0).read().split());b=[] 
for p in range(1,101): 
 c=sum(a[i]>=p or any(a[j]>=p for j in(i-1,i+1)if 0<=j<n)for i in range(n)) 
 if 0<c<=k:b+=[(c,p)] 
print(max(b)[1]if b else min(a)-1)