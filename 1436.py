N = int(input())
cnt = 0


for i in range(666, 10000000):
    if '666' in str(i):
        cnt += 1
            
    else:
        continue
    
    if cnt == N:
        print(i)
        break
