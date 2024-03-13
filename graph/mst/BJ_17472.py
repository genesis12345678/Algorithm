import copy
import sys
from collections import deque
from queue import PriorityQueue

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
myMap = [[0 for _ in range(m)] for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    myMap[i] = list(map(int, input().split()))

num = 1
sumList = list([])  # 모든 섬 정보 리스트
mlist = []  # 각각의 섬 정보 리스트, BFS를 통해 하나의 mlist가 sumList의 한 공간에 들어간다.


def addNode(i, j, qu):
    myMap[i][j] = num
    visit[i][j] = True
    temp = [i, j]
    mlist.append(temp)
    qu.append(temp)


def BFS(i, j):
    queue = deque()
    mlist.clear()
    start = [i, j]
    queue.append(start)
    mlist.append(start)

    visit[i][j] = True
    myMap[i][j] = num

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if not visit[nx][ny] and myMap[nx][ny] != 0:
                    addNode(nx, ny, queue)

    return mlist


for i in range(n):
    for j in range(m):
        if myMap[i][j] != 0 and not visit[i][j]:
            tempList = copy.deepcopy(BFS(i, j))
            num += 1  # 섬 번호
            sumList.append(tempList)

pq = PriorityQueue()

for now in sumList:
    for temp in now:
        x = temp[0]
        y = temp[1]

        now_S = myMap[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            blength = 0
            while nx >= 0 and nx < n and ny >= 0 and ny < m:

                if myMap[nx][ny] == now_S:
                    break

                elif myMap[nx][ny] != 0:
                    if blength > 1:
                        pq.put((blength, now_S, myMap[nx][ny]))
                    break

                else:
                    blength += 1

                nx += dx[i]
                ny += dy[i]


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


parent = [0] * num

for i in range(len(parent)):
    parent[i] = i

useEdge = 0
result = 0

while pq.qsize() > 0:
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1

if useEdge == num - 2:
    print(result)
else:
    print(-1)
