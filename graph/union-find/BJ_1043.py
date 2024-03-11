n, m = map(int, input().split())
trues = list(map(int, input().split()))
t = trues[0]

party = [[] for _ in range(m)]
result = 0


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


for i in range(m):
    party[i] = list(map(int, input().split()))

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    first = party[i][1]
    for j in range(2, len(party[i])):
        union(first, party[i][j])

for i in range(m):
    isPossible = True
    first = party[i][1]

    for j in range(1, len(trues)):
        if find(first) == find(trues[j]):
            isPossible = False
            break

    if isPossible:
        result += 1

print(result)
