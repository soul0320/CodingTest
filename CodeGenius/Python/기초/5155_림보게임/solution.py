N = int(input()) 
heights = list(map(int, input().split())) 
 
for h in heights: 
    if h <= 160: 
        print(f"I {h}") 
        break 
else: 
    print("P")