import sys
from collections import deque

input = sys.stdin.readline


class Node:

    def __init__(self, next_node, dist):
        self.next_node = next_node
        self.dist = dist


n = int(input())
m = int(input())

A = [[] for _ in range(n + 1)]
reverseA = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)

for i in range(m):
    S, E, V = map(int, input().split())
    A[S].append(Node(E, V))
    reverseA[E].append(Node(S, V))
    inDegree[E] += 1

start, end = map(int, input().split())


qu = deque()
qu.append(start)
result = [0] * (n + 1)

while qu:
    now = qu.popleft()
    for next in A[now]:
        inDegree[next.next_node] -= 1

        result[next.next_node] = max(result[next.next_node], result[now] + next.dist)

        if inDegree[next.next_node] == 0:
            qu.append(next.next_node)


count = 0
visit = [False] * (n + 1)
qu.clear()
qu.append(end)
visit[end] = True

while qu:
    now = qu.popleft()
    for next in reverseA[now]:
        if result[next.next_node] + next.dist == result[now]:
            count += 1

            if not visit[next.next_node]:
                visit[next.next_node] = True
                qu.append(next.next_node)

print(result[end])
print(count)