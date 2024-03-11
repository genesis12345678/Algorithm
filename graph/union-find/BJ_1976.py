n = int(input())
m = int(input())
city = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    city[i][1:] = list(map(int, input().split()))

route = list(map(int, input().split()))

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if city[i][j] == 1:  # 두 도시가 연결되어 있다면 union 수행
            union(i, j)


index = find(route[0])

isConnect = True
for i in range(1, m):
    if index != find(route[i]):
        isConnect = False
        break

if isConnect:
    print("YES")
else:
    print("NO")