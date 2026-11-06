n,*a=open(0).read().split();a.sort(reverse=1);s=''.join(a) 
print(0 if s[0]=='0'else s if a.count('0')>1 and sum(map(int,a))%3<1 else -1)