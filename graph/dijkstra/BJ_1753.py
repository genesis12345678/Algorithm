import sys
from queue import PriorityQueue

input = sys.stdin.readline


class Node:
    def __init__(self, node, dist):
        self.node = node
        self.dist = dist


V, E = map(int, input().split())
k = int(input())

distance = [sys.maxsize] * (V + 1)
visit = [False] * (V + 1)
A = [[] for _ in range(V + 1)]

pq = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    A[u].append(Node(v, w))

pq.put((0, k))
distance[k] = 0

while pq.qsize() > 0:
    now = pq.get()

    if visit[now[1]]:
        continue
    visit[now[1]] = True

    for next in A[now[1]]:
        next_node = next.node
        dist = next.dist

        if distance[next_node] > distance[now[1]] + dist:

            distance[next_node] = distance[now[1]] + dist
            pq.put((distance[next_node], next_node))

result = []

for i in range(1, V + 1):
    result.append(str(distance[i]) if visit[i] else "INF")

print("\n".join(result))
