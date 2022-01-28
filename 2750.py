N = int(input())

num_list = []

for i in range(N):
    num_list.append(int(input()))

for i in range(1, N):
    for j in range(i, 0, -1):
        if num_list[j-1] > num_list[j]:
            num_list[j-1], num_list[j] = num_list[j], num_list[j-1]

for k in range(N):
    print(num_list[k])
