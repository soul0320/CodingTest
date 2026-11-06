n,m=map(int,input().split());g=[input().split()for _ in range(n)] 
print(max(sum('0'not in r for r in g),sum('0'not in c for c in zip(*g))))