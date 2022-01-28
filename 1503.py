arr = list(range(1,1001))
ans = 1000
N, M = input("").split()

N = int(N)
M = int(M)

S = list(map(int, input().split()))

S_of_difference = list(set(arr) - set(S))

if N <= (min(S_of_difference) ** 3):
    print(abs(N - (min(S_of_difference) ** 3)))
    
else:
    for i in range(0, 1000 - M):
        x = S_of_difference[i]
        for j in range(i, 1000 - M):
            y = S_of_difference[j]
            for k in range(j, 1000 - M):
                z = S_of_difference[k]
                ans = min(ans, abs(N-(x*y*z)))

    print(ans)
