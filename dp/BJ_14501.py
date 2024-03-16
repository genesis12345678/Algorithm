import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 2)

T = [0] * (N + 1)   # 상담 시간
P = [0] * (N + 1)   # 상담 수입

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

for i in range(N, 0, -1):
    if i + T[i] > N + 1:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + T[i]] + P[i])

print(dp[1])
