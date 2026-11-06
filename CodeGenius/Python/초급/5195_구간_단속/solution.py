L,n,*a=open(0).read().split();s={} 
for i in range(0,len(a),2):c,h=a[i],a[i+1];s[c]=int(h[:2])*3600+int(h[3:5])*60+int(h[6:])-s.get(c,0) 
for c in sorted(s):print(c,int(L)*3600//s[c])