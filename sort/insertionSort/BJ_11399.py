n = int(input())
a = list(map(int, input().split()))
s = [0] * n

for i in range(1, n):
    insert_point = i
    insert_value = a[i]
    for j in range(i-1, -1, -1):  # i-1부터 0까지 -1씩 감소하면서 반복
        if a[j] < a[i]:
            insert_point = j + 1  # j위치 바로 다음에 위치해야 하므로 +1
            break
        if j == 0:  # j가 0까지 왔다는 것은 비교할 데이터가 가장 작은 값이라는 의미
            insert_point = 0
    for j in range(i, insert_point, -1):  # 삽입을 위해 현재 위치에서 insert_point 까지 한 칸씩 뒤로 밀기
        a[j] = a[j-1]
    a[insert_point] = insert_value  # 삽입 위치에 현재 데이터 저장

s[0] = a[0]
total = s[0]

for i in range(1, n):
    s[i] = s[i-1] + a[i]
    total += s[i]

print(total)