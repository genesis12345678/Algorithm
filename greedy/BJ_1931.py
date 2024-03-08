n = int(input())
A = [[0] * 2 for _ in range(n)]

for i in range(n):
    start, end = map(int, input().split())
    A[i][0] = end  # 종료 시각 우선 정렬이 먼저이므로 0번째에 종료 시각을 먼저 저장
    A[i][1] = start

A.sort()
count = 0
end = -1

for i in range(n):
    if A[i][1] >= end:
        end = A[i][0]
        count += 1

print(count)
