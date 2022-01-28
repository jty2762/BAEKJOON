N = input()
N_len = len(str(N))
N = int(N)

min_value = 1000000

for i in range(N, 0, -1):
    N_list = list()
    tmp = 0
    N_list.insert(0,i)
    for j in range(1, N_len + 1):
        if(N_len != j):
            N_list.insert(j, i // (10**(N_len - j)))
            i -= N_list[j]*(10**(N_len - j))
        else:
            N_list.insert(j, i % 10)
    for k in range(0, N_len + 1):
        tmp += N_list[k]
    if(N == tmp):
        min_value = min(min_value, N_list[0])
    else:
        continue

if(min_value == 1000000):
    print(0)
else:
    print(min_value)
