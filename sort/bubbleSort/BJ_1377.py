import sys

input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append((int(input()), i))  # [data, index] 튜플 저장  # 먼저 넣은 데이터를 기준으로 정렬을 시도한다.

max_val = 0
a.sort()

for i in range(n):
    # a[i][1] = 각 튜플의 index
    if a[i][1] - i > max_val:  # 정렬 전 index - 정렬 후 index 계산의 최댓값 저장
        max_val = a[i][1] - i

print(max_val + 1)


