n=int(input()) 
while n%2==0:n//=2 
for p in(3,5,17,257,65537): 
 if n%p==0:n//=p 
print('YES'if n==1 else'NO')