import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
visit = [False] * n
tree = [[] for _ in range(n)]
p = list(map(int, input().split()))
ans = 0
root = 0

for i in range(n):
    if(p[i] != -1):
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i


def DFS(node):
    global ans
    visit[node] = True
    child = 0

    for next in tree[node]:
        if not visit[next] and next != deleteNode:
            child += 1
            DFS(next)

    if child == 0:
        ans += 1


deleteNode = int(input())

if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(ans)
