n,*v=map(int,open(0).read().split());d=v[::2];a=v[1::2] 
print(min(range(n),key=lambda i:sum(a[j]*abs(d[i]-d[j])for j in range(n)))+1)