y,b,s,r=input().split();y=int(y) 
print(0 if y<1 else 28 if r<'P'else 20 if y>4 else 28 if s>'N'or b=='ROKAF'else 32)