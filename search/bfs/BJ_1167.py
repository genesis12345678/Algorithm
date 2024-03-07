from collections import deque

v = int(input())
A = [[] for _ in range(v + 1)]

for _ in range(v):
    data = list(map(int, input().split()))
    index = 0
    s = data[index]  # 기준 노드
    index += 1
    while True:
        e = data[index]  # 기준 노드와 연결된 노드
        if e == -1:
            break
        d = data[index + 1]  # 거리
        A[s].append((e, d))  # [노드, 거리] 튜플
        index += 2

distance = [0] * (v + 1)
visit = [False] * (v + 1)


def BFS(node):
    queue = deque()
    queue.append(node)
    visit[node] = True

    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visit[i[0]]:
                visit[i[0]] = True
                queue.append(i[0])

                distance[i[0]] = distance[now_node] + i[1]


BFS(1)
Max = 1

for i in range(2, v + 1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (v + 1)
visit = [False] * (v + 1)

BFS(Max)
distance.sort()
print(distance[v])
