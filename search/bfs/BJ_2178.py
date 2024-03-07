from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
A = [[0] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]

for i in range(n):
    numbers = list(input())
    for j in range(m):
        A[i][j] = int(numbers[j])


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True

    while queue:
        now = queue.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if A[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    A[nx][ny] = A[now[0]][now[1]] + 1
                    queue.append((nx, ny))


BFS(0, 0)
print(A[n-1][m-1])
