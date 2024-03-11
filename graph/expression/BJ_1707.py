import sys

input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

n = int(input())
isEven = True


def DFS(node):
    global isEven
    visit[node] = True

    for next in A[node]:
        if not visit[next]:
            check[next] = (check[node] + 1) % 2
            DFS(next)

        elif check[node] == check[next]:
            isEven = False


for _ in range(n):
    v, e = map(int, input().split())
    A = [[] for _ in range(v + 1)]
    visit = [False] * (v + 1)
    check = [0] * (v + 1)
    isEven = True

    for i in range(e):
        u, v = map(int, input().split())
        A[u].append(v)
        A[v].append(u)

    for i in range(1,  v + 1):
        if isEven:
            DFS(i)
        else:
            break

    if isEven:
        print("YES")
    else:
        print("NO")
