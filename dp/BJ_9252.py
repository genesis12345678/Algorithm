import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

A = list(input())
B = list(input())

A.pop()  # "\n" 문자열 제거
B.pop()  # "\n" 문자열 제거

dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
result = []

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(A)][len(B)])


def getText(row, col):
    if row == 0 or col == 0:
        return

    if A[row - 1] == B[col - 1]:
        result.append(A[row - 1])  # 둘은 같으니 A[row-1]이나 B[col-1]중 아무거나 저장해도 됨
        getText(row - 1, col - 1)
    else:
        if dp[row - 1][col] > dp[row][col - 1]:  # 왼쪽 값이랑 위쪽 값 중 더 큰 값으로 이동
            getText(row - 1, col)
        else:
            getText(row, col - 1)


getText(len(A), len(B))

# for i in range(len(result) - 1, -1, -1):
#     print(result.pop(i), end='')

for _ in range(len(result)):
    print(result.pop(), end='')