n=input() 
print(sum(n in f'{i//3600:02}{i//60%60:02}{i%60:02}' for i in range(86400)))