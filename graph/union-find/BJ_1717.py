import sys

input = sys.stdin.readline
sys.setrecursionlimit(100_000)

n, m = map(int, input().split())
parent = [0] * (n + 1)


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


def checkSame(a, b):
    a = find(a)
    b = find(b)
    return a == b

for i in range(0, n + 1):
    parent[i] = i

result = []

for i in range(m):
    q, a, b = map(int, input().split())

    if q == 0:
        union(a, b)
    else:
        result.append("YES" if checkSame(a, b) else "NO")

print("\n".join(result))
