N = int(input())
people_list = [[0 for col in range(2)]for row in range(N)]
count = [1 for i in range(N)]

for i in range(0,N):
    people_list[i] = list(map(int, input().split()))

for i in range(0,N):
    for j in range(0,N):
        if(i == j):
            continue
        elif(people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]):
            count[i] += 1

for i in range(0,N):
    print(count[i], end=' ')
        
    
