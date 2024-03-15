n, k = map(int, input().split())
DP = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    DP[i][1] = i
    DP[i][0] = 1
    DP[i][i] = 1

for i in range(2, n + 1):
    for j in range(1, i):
        DP[i][j] = DP[i - 1][j] + DP[i - 1][j - 1]
        DP[i][j] %= 10_007

print(DP[n][k])