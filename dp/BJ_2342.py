import sys

input = sys.stdin.readline
dp = [[[sys.maxsize for _ in range(5)] for _ in range(5)] for _ in range(100_001)]

mp = [
    [0, 2, 2, 2, 2],  # 0에 있던 발이 0, 1, 2, 3, 4번으로 이동할 때 드는 힘
    [2, 1, 3, 4, 3],  # 1에 있던 발이 0, 1, 2, 3, 4번으로 이동할 때 드는 힘
    [2, 3, 1, 3, 4],  # 2에 있던 발이 0, 1, 2, 3, 4번으로 이동할 때 드는 힘
    [2, 4, 3, 1, 3],  # 3에 있던 발이 0, 1, 2, 3, 4번으로 이동할 때 드는 힘
    [2, 3, 4, 3, 1]]  # 4에 있던 발이 0, 1, 2, 3, 4번으로 이동할 때 드는 힘

dp[0][0][0] = 0
inputList = list(map(int, input().split()))

s = 1
index = 0

while inputList[index] != 0:
    n = inputList[index]

    for i in range(5):
        if n == i:  # 두 발이 같은 자리에 있을 수 없다.
            continue

        for j in range(5):  # 오른발을 옮겨 현재 모습이 됐을 때 최소 힘 저장
            dp[s][i][n] = min(dp[s][i][n], dp[s - 1][i][j] + mp[j][n])

    for j in range(5):
        if n == j:
            continue
        for i in range(5):
            dp[s][n][j] = min(dp[s][n][j], dp[s - 1][i][j] + mp[i][n])

    s += 1
    index += 1

s -= 1
result = sys.maxsize

for i in range(5):
    for j in range(5):
        result = min(result, dp[s][i][j])

print(result)
