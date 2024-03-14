import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
visit = [False] * (n + 1)
tree = [[] for _ in range(n + 1)]
ans = [0] * (n + 1)

for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)


def DFS(parent):
    visit[parent] = True

    for next in tree[parent]:
        if not visit[next]:
            ans[next] = parent
            DFS(next)


DFS(1)

result = []
for i in range(2, n + 1):
    result.append(str(ans[i]))

print("\n".join(result))