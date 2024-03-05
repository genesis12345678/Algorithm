n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

for i in range(n - 1):  # 0 ~ n-1 : 0, 1, 2, 3
    for j in range(n - 1 - i):  # 반복이 진행 될수록 마지막 데이터는 정렬 되기 때문에 마지막에 i만큼 빼준다.
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

for i in range(n):
    print(a[i])

