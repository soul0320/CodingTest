a=[input().split() for i in range(int(input()))] 
a.sort(key=lambda x:-int(x[1])) 
for x in a[:3]:print(x[0])