import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
visit = [False] * (n+1)


def dfs(node):
    visit[node] = True
    for i in a[node]:
        if not visit[i]:
            dfs(i)


for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)  # 양방향 연결
    a[v].append(u)

count = 0

for i in range(1, n+1):
    if not visit[i]:
        count += 1
        dfs(i)

print(count)
