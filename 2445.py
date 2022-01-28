N = int(input(""))

def starprint(N, i):
    print('*' * i, end = '')
    print(' ' * (2*(N - i)), end = '')
    print('*' * i)

for i in range(1, N+1):
    starprint(N, i)

for j in range(N-1, 0, -1):
    starprint(N, j)
