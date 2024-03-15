import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (n + 1)
parent = [0] * (n + 1)
visit = [False] * (n + 1)


def DFS(node, level):
    visit[node] = True
    depth[node] = level

    for next in tree[node]:
        if not visit[next]:

            parent[next] = node
            DFS(next, level + 1)


def BFS(node):
    qu = deque()
    qu.append(node)
    visit[node] = True
    level = 1
    nowSize = 1  # 현재 depth(level) 크기
    count = 0  # 현재 depth 에서 몇 개 노드를 처리했는지 알려주는 변수

    while qu:
        nowNode = qu.popleft()
        for next in tree[nowNode]:
            if not visit[next]:
                visit[next] = True
                qu.append(next)

                parent[next] = nowNode  # 부모 노드 저장
                depth[next] = level  # 노드 깊이 저장

        count += 1
        if count == nowSize:  # 다음 깊이로 가기 위한 처리
            count = 0
            nowSize = len(qu)
            level += 1


# BFS(1)
DFS(1, 0)


def LCA(a, b):
    if depth[a] < depth[b]:  # 무조건 a의 depth를 더 깊게 하기 위해
        a, b = b, a  # a, b swap - 파이썬 문법

    while depth[a] != depth[b]:  # depth 맞추기
        a = parent[a]

    while a != b:  # 공통 조상 찾기
        a = parent[a]
        b = parent[b]

    return a  # a와 b가 같아졌으니 둘 중 아무거나 리턴


m = int(input())

result = []

for _ in range(m):
    a, b = map(int, input().split())
    result.append(str(LCA(a, b)))

print("\n".join(result))
