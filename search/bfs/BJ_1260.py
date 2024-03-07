from collections import deque

n, m, start = map(int, input().split())
A = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

for i in range(n + 1):
    A[i].sort()


def dfs(node):
    print(node, end=' ')
    visit[node] = True
    for i in A[node]:
        if not visit[i]:
            dfs(i)


visit = [False] * (n + 1)
dfs(start)


def bfs(node):
    queue = deque()
    queue.append(node)
    visit[node] = True

    while queue:
        now_node = queue.popleft()
        print(now_node, end=' ')

        for i in A[now_node]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)


print()
visit = [False] * (n + 1)
bfs(start)
