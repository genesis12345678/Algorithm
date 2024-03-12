import heapq
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
A = [[] for _ in range(n + 1)]
distance = [[sys.maxsize] * k for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    A[a].append((b, c))

pq = [(0, 1)]  # (가중치, 노드)   가중치 우선
distance[1][0] = 0

while pq:
    cost, node = heapq.heappop(pq)
    for next_node, next_cost in A[node]:
        new_cost = cost + next_cost

        if distance[next_node][k - 1] > new_cost:
            distance[next_node][k - 1] = new_cost

            distance[next_node].sort()  # 정렬로 인해 거리 순으로 변경됨
            heapq.heappush(pq, [new_cost, next_node])


result = []
for i in range(1, n + 1):
    if distance[i][k-1] == sys.maxsize:
        result.append(str(-1))
    else:
        result.append(str(distance[i][k-1]))

print("\n".join(result))