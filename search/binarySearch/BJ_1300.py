n = int(input())
k = int(input())

start = 1
end = k
result = 0

while start <= end:
    mid = int((start + end) / 2)
    count = 0  # 중앙값보다 작은 수의 개수

    for i in range(1, n + 1):  # 중앙값보다 작은 수 계산
        count += min(int(mid / i), n)

    if count < k:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)