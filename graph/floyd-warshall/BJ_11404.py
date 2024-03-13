import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
distance = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    distance[i][i] = 0

for i in range(m):
    start, end, v = map(int, input().split())
    if distance[start][end] > v:  # 노선이 여러개 일 때 비용이 더 적은 정보 저장
        distance[start][end] = v

for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if distance[s][e] > distance[s][k] + distance[k][e]:
                distance[s][e] = distance[s][k] + distance[k][e]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')

    print()
