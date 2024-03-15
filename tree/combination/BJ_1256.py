import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
dp = [[0 for _ in range(201)] for _ in range(201)]  # n + m개 중에서 조합을 골라야 하므로 n, m의 최댓값은 100, 그래서 200크기로 생성

for i in range(201):
    for j in range(0, i + 1):
        # 0개를 뽑는 경우의 수와 i개 중에 i개를 뽑는 경우의 수는 1이다.
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            if dp[i][j] > 1_000_000_000:
                dp[i][j] = 1_000_000_000  # k 최대 범위를 벗어나면 범위의 최댓값 저장

if dp[n + m][m] < k:
    print(-1)
else:
    while not (n == 0 and m == 0):
        if dp[n - 1 + m][m] >= k:  # a를 선택해도 남는 경우의 수가 k보다 큰 경우
            print("a", end='')
            n -= 1
        else:
            print("z", end='')
            k -= dp[n - 1 + m][m]  # n - 1 + m: n(a의 개수)에서 1개를 선택하고 남은 m(z의 개수)를 더한 것, 즉 a를 선택하고 남은 문자 총 개수
            m -= 1
