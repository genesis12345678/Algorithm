import sys

n, m = map(int, input().split())
distance = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    distance[i][i] = 0

for i in range(m):
    s, e = map(int, input().split())
    distance[s][e] = 1
    distance[e][s] = 1

for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if distance[s][e] > distance[s][k] + distance[k][e]:
                distance[s][e] = distance[s][k] + distance[k][e]

min = sys.maxsize
ans = 0

for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        temp += distance[i][j]

    if min > temp:
        min = temp
        ans = i

print(ans)
