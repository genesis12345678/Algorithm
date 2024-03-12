import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    inDegree[b] += 1

qu = deque()

for i in range(1, n + 1):
    if inDegree[i] == 0:
        qu.append(i)


result = []

while qu:
    now = qu.popleft()
    result.append(str(now))

    for next in A[now]:
        inDegree[next] -= 1
        if inDegree[next] == 0:
            qu.append(next)

print(" ".join(result))
