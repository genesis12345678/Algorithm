N = int(input())
mod = 1_000_000_000
dp = [[0 for _ in range(11)] for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]

    for j in range(1, 9):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod

sum = 0

for i in range(0, 10):
    sum = (sum + dp[N][i]) % mod

print(sum)
