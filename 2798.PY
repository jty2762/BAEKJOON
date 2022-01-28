N,M = map(int, input().split())

N_list = list(map(int, input().split()))

max_num = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tmp = N_list[i] + N_list[j] + N_list[k]
            if(tmp > M):
                continue
            else:
                max_num = max(max_num,tmp)

print(max_num)
