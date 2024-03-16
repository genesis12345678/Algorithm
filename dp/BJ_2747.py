N = int(input())
dp = [-1] * (N + 1)
dp[0] = 0  # 초기화할 수 있는 초깃값
dp[1] = 1  # 초기화할 수 있는 초깃값


def fibo(n):
    if dp[n] != -1:
        return dp[n]

    dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]


fibo(N)
print(dp[N])
