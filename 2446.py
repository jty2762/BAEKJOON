N = int(input(""))

def starprint(N, i):
    print(' ' * i, end = '')
    print('*' * (N+(N-1)), end = '')
    print(' ' * i)

for i in range(0, N-1):
    starprint(N-i, i)

print(' ' * (N-1), end = '')
print('*', end = '')
print(' ' * (N-1))

for j in range(N-2, -1, -1):
    starprint(N-j, j)
