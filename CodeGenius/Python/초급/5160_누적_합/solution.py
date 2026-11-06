n,*a=map(int,open(0).read().split()) 
s=1 
while s<n:s*=2 
a+=[0]*(s-n);r=[] 
while a:r=[a]+r;a=[a[i]+a[i+1]for i in range(0,len(a)-1,2)] 
for l in r:print(*l,end=' \n')