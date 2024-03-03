import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
result = 0

S[0] = A[0]

for i in range(1, n):
    S[i] = S[i - 1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        result += 1
    C[remainder] += 1

for i in range(m):
    if C[i] >= 2:
        # result += (C[i] * (C[i] - 1)) // 2
        result += int(math.factorial(C[i]) / (math.factorial(C[i] - 2) * 2))

print(result)