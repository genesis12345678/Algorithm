import sys

input = sys.stdin.readline
N = int(input())
M = []
dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

M.append((0, 0))  # 1번부터 index를 맞추기 위해

for _ in range(N):
    x, y = map(int, input().split())
    M.append((x, y))


def solution(s, e):
    result = sys.maxsize

    if dp[s][e] != -1:  # 메모이제이션
        return dp[s][e]

    if s == e:  # 행렬이 1개
        return 0

    if s + 1 == e:  # 행렬이 2개
        return M[s][0] * M[s][1] * M[e][1]

    # 행렬이 3개 이상
    for i in range(s, e):
        alpha = M[s][0] * M[i][1] * M[e][1]
        result = min(result, alpha + solution(s, i) + solution(i + 1, e))

    dp[s][e] = result
    return dp[s][e]


print(solution(1, N))
