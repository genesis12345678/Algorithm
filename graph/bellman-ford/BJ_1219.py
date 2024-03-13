import sys

input = sys.stdin.readline

n, startCity, endCity, m = map(int, input().split())
edges = []
distance = [-sys.maxsize] * n  # 작은 수로 초기화

for _ in range(m):
    s, e, c = map(int, input().split())  # 시작, 끝, 가격
    edges.append((s, e, c))

cityMoney = list(map(int, input().split()))

distance[startCity] = cityMoney[startCity]

for i in range(n + 51):
    for start, end, cost in edges:
        if distance[start] == -sys.maxsize:  # 출발 노드가 미방문 노드
            continue

        elif distance[start] == sys.maxsize:  # 출발 노드가 양수 사이클이면 도착 노드도 양수 사이클
            distance[end] = sys.maxsize

        elif distance[end] < distance[start] + cityMoney[end] - cost:
            distance[end] = distance[start] + cityMoney[end] - cost

            if i >= n - 1:  # n-1번 이후에 업데이트 된 것이라면 양수 사이클
                distance[end] = sys.maxsize


print(distance)

if distance[endCity] == -sys.maxsize:
    print("gg")
elif distance[endCity] == sys.maxsize:
    print("Gee")
else:
    print(distance[endCity])
