number_divisor = int(input(""))

real_divisor = list(map(int, input().split()))
    
if number_divisor == 0:
    print("error")

else:
    N = min(real_divisor) * max(real_divisor)

print(N)
            
            
    
    
