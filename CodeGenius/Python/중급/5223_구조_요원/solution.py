n=int(input());x,y=map(int,input().split());b=0;v=9e9 
for t in range(min(0,x),max(0,x)+1): 
 c=(t*t+n*n)**.5+2*((x-t)**2+y*y)**.5 
 if c<v-1e-9:v=c;b=t 
print(b)