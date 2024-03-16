import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
dp[1] = 0  # 굳이 초기화할 필요는 없지만 명시적으로 표시

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
