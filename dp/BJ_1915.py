import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(n):
    data = list(input().strip())  # strip() : 공백 제거
    dp[i] = [int(x) for x in data]

Max = -sys.maxsize

for i in range(n):
    for j in range(m):
        if int(dp[i][j]) == 1 and i > 0 and j > 0:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        Max = max(Max, dp[i][j])

print(Max * Max)
