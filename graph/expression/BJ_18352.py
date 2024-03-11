import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
A = [[] for _ in range(n + 1)]
ans = []
visit = [-1] * (n + 1)


def BFS(node):
    queue = deque()
    queue.append(node)

    visit[node] += 1

    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if visit[i] == -1:
                visit[i] = visit[now_node] + 1
                queue.append(i)


for _ in range(m):
    start, end = map(int, input().split())
    A[start].append(end)

BFS(x)

for i in range(1, n + 1):
    if visit[i] == k:
        ans.append(i)

result = []

if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        result.append(str(i))

print("\n".join(result))
