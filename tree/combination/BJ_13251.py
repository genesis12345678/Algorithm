m = int(input())  # 색깔 개수
stone = list(map(int, input().split()))  # 색깔별 조약돌 개수
probability = [0] * 51  # 색깔별 확률
sum = 0  # 전체 조약돌 개수

for i in range(m):
    sum += stone[i]

k = int(input())  # 선택한 조약돌 개수

result = 0
for i in range(m):
    if stone[i] >= k:  # 최소한 조약돌이 선택한 조약돌의 개수보다 크거나 같아야 뽑힐 확률이 있다.
        probability[i] = 1

        for j in range(k):
            probability[i] *= (stone[i] - j) / (sum - j)

        result += probability[i]

print(result)
