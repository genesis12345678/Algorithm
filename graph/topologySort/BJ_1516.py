from collections import deque

n = int(input())
A = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)
build = [0] * (n + 1)

for i in range(1, n + 1):
    inputList = list(map(int, input().split()))
    build[i] = inputList[0]
    index = 1

    while True:
        temp = inputList[index]
        index += 1

        if temp == -1:
            break

        A[temp].append(i)
        inDegree[i] += 1

qu = deque()

for i in range(1, n + 1):
    if inDegree[i] == 0:
        qu.append(i)

result = [0] * (n + 1)

while qu:
    now = qu.popleft()
    for next in A[now]:
        inDegree[next] -= 1

        result[next] = max(result[next], result[now] + build[now])

        if inDegree[next] == 0:
            qu.append(next)

for i in range(1, n + 1):
    print(result[i] + build[i])
