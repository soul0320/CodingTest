n=int(input());s=0 
for x in(50000,10000,5000,1000,500,100,50,10,1):s+=n//x;n%=x 
print(s)