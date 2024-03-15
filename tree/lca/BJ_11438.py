import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (n + 1)
visit = [False] * (n + 1)
temp = 1
kmax = 0

while temp <= n:
    temp <<= 1  # shift 연산
    kmax += 1

parent = [[0 for _ in range(n + 1)] for _ in range(kmax + 1)]


def BFS(node):
    qu = deque()
    qu.append(node)
    visit[node] = True
    level = 1
    nowSize = 1
    count = 0

    while qu:
        nowNode = qu.popleft()
        for next in tree[nowNode]:
            if not visit[next]:
                visit[next] = True
                qu.append(next)

                parent[0][next] = nowNode
                depth[next] = level

        count += 1
        if count == nowSize:
            count = 0
            nowSize = len(qu)
            level += 1


BFS(1)

# 점화식으로 부모 노드 리스트 채우기
for k in range(1, kmax + 1):
    for n in range(1, n + 1):
        parent[k][n] = parent[k - 1][parent[k - 1][n]]


def LCA(a, b):
    if depth[a] > depth[b]:  # 더 깊은 depth가 b가 되도록
        a, b = b, a

    # 깊이 빠르게 맞추기
    for k in range(kmax, -1, -1):
        if pow(2, k) <= depth[b] - depth[a]:    # 두 노드의 depth 차이가 2^k보다 크면
            b = parent[k][b]                    # b의 depth를 2^k 만큼 한 번에 이동

    # 조상 빠르게 찾기
    for k in range(kmax, -1, -1):
        if a == b:
            break
        if parent[k][a] != parent[k][b]:        # 부모 노드가 다르면 2^k 만큼 한 번에 이동
            a = parent[k][a]
            b = parent[k][b]

    lca = a
    if a != b:      # a와 b가 다르면 한 칸만 부모 노드로 이동
        lca = parent[0][lca]

    return lca


m = int(input())

result = []
for _ in range(m):
    s, e = map(int, input().split())
    result.append(str(LCA(s, e)))

print("\n".join(result))