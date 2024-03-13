import sys
from queue import PriorityQueue

input = sys.stdin.readline
n, m = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    s, e, v = map(int, input().split())
    pq.put((v, s, e))  # 순서에 의해 정렬 순서가 결정되므로 가중치를 먼저 넣어야 한다.


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


useEdge = 0
result = 0

while useEdge < n - 1:
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1

print(result)