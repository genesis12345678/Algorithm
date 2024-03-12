import sys
from queue import PriorityQueue

input = sys.stdin.readline


class Node:
    def __init__(self, node, dist):
        self.node = node
        self.dist = dist


n = int(input())
m = int(input())

A = [[] for _ in range(n + 1)]
distance = [sys.maxsize] * (n + 1)
visit = [False] * (n + 1)

for i in range(m):
    S, E, V = map(int, input().split())
    A[S].append(Node(E, V))

start, end = map(int, input().split())


def dijkstra(start, end):
    pq = PriorityQueue()
    pq.put((0, start))
    distance[start] = 0

    while pq.qsize() > 0:
        now = pq.get()
        now_node = now[1]

        if not visit[now_node]:
            visit[now_node] = True

            for next in A[now_node]:
                if not visit[next.node] and distance[next.node] > distance[now_node] + next.dist:
                    distance[next.node] = distance[now_node] + next.dist
                    pq.put((distance[next.node], next.node))

    return distance[end]


print(dijkstra(start, end))

