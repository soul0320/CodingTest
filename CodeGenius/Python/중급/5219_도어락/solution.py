n,*t=map(int,open(0).read().split());M=10**9+7;d=[1]*9 
w=lambda a,b:1 if a==b else 2 if max(abs(a//3-b//3),abs(a%3-b%3))<2 else 3 
for x in t:d=[sum(d[a]for a in range(9)if w(a,b)==x)%M for b in range(9)] 
print(sum(d)%M)