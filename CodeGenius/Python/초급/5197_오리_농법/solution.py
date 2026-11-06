n=int(input());g=[input().split()for _ in range(n)];c=[*zip(*g)] 
print(sum(g[i][j]=='2'and'1'in g[i]and'1'in c[j]for i in range(n)for j in range(n)))