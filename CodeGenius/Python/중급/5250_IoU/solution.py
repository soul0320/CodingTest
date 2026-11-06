n=int(input());r=[list(map(int,input().split()))for _ in range(n)];B,U=-1,1 
for i in range(n): 
 for j in range(i+1,n): 
  x,y,w,h=r[i];a,c,d,e=r[j] 
  I=max(0,min(x+w,a+d)-max(x,a))*max(0,min(y+h,c+e)-max(y,c));u=w*h+d*e-I 
  if I*U>B*u:B,U=I,u;p=(i+1,j+1) 
print(*p)