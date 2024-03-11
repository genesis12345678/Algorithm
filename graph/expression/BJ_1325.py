import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
ans = [0] * (n + 1)


def BFS(node):
    queue = deque()
    queue.append(node)

    visit = [False] * (n + 1)
    visit[node] = True

    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visit[i]:
                visit[i] = True
                ans[i] += 1
                queue.append(i)


for i in range(m):
    a, b = map(int, input().split())
    A[a].append(b)

for i in range(1, n + 1):
    BFS(i)

maxVal = max(ans)

result = []
for i in range(1, n + 1):
    if ans[i] == maxVal:
        result.append(str(i))

print(" ".join(result))
