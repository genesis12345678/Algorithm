n = int(input())
distance = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    distance[i] = list(map(int, input().split()))

for k in range(n):
    for s in range(n):
        for e in range(n):
            if distance[s][k] == 1 and distance[k][e] == 1:
                distance[s][e] = 1

for i in range(n):
    for j in range(n):
        print(distance[i][j], end=' ')
    print()
