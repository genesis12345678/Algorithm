import sys

input = sys.stdin.readline
N = int(input())
W = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    W[i] = list(map(int, input().split()))

dp = [[0 for _ in range(1 << 16)] for _ in range(16)]  # 1 << 16 = 2^16


def solution(c, v):
    if v == (1 << N) - 1:
        if W[c][0] == 0:
            return sys.maxsize
        else:
            return W[c][0]

    if dp[c][v] != 0:
        return dp[c][v]

    minValue = sys.maxsize

    for i in range(N):
        if (v & (1 << i)) == 0 and W[c][i] != 0:
            minValue = min(minValue, solution(i, (v | (1 << i))) + W[c][i])

    dp[c][v] = minValue
    return dp[c][v]


print(solution(0, 1))
