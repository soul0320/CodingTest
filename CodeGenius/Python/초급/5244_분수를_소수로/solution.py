import sys 
try:sys.set_int_max_str_digits(0) 
except:0 
p,q,n=map(int,open(0).read().split());x=(2*p*10**n+q)//(2*q);m=10**n 
print(f"{x//m}.{str(x%m).zfill(n)}")