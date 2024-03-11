# 두 리스트를 이용하여 6가지 이동 케이스 정의
# 0=A, 1=B, 2=C
from collections import deque

send = [0, 0, 1, 1, 2, 2]
receive = [1, 2, 0, 2, 0, 1]

now = list(map(int, input().split()))
visit = [[False for j in range(201)] for i in range(201)]
ans = [False] * 201


def BFS():
    qu = deque()
    qu.append((0, 0))
    visit[0][0] = True
    ans[now[2]] = True

    while qu:
        now_node = qu.popleft()
        A = now_node[0]
        B = now_node[1]
        C = now[2] - A - B

        for i in range(6):
            next = [A, B, C]
            next[receive[i]] += next[send[i]]
            next[send[i]] = 0

            if next[receive[i]] > now[receive[i]]:
                next[send[i]] = next[receive[i]] - now[receive[i]]
                next[receive[i]] = now[receive[i]]

            if not visit[next[0]][next[1]]:
                visit[next[0]][next[1]] = True
                qu.append((next[0], next[1]))

                if next[0] == 0:
                    ans[next[2]] = True


BFS()

for i in range(len(ans)):
    if ans[i]:
        print(i, end=' ')
