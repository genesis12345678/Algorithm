import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
arrive = False
A = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)


def dfs(node, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visit[node] = True
    for i in A[node]:
        if not visit[i]:
            dfs(i, depth + 1)

    visit[node] = False


for i in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

for i in range(n):
    dfs(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)