import sys

input = sys.stdin.readline
result = 0

n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)  # 0번째에 값 0을 삽입
temp = [0] * (n + 1)


def merge_sort(start, end):
    global result

    if end - start < 1:
        return

    mid = int((start + end) / 2)
    merge_sort(start, mid)
    merge_sort(mid + 1, end)

    for i in range(start, end + 1):
        temp[i] = a[i]

    k = start
    index1 = start
    index2 = mid + 1

    while index1 <= mid and index2 <= end:
        if temp[index1] > temp[index2]:
            a[k] = temp[index2]
            result += index2 - k  # 뒤쪽 데이터가 이동할 때에만 결과를 더해준다.  # index2 - k: 앞에 남아 있는 데이터 개수
            k += 1
            index2 += 1
        else:
            a[k] = temp[index1]
            k += 1
            index1 += 1

    while index1 <= mid:
        a[k] = temp[index1]
        k += 1
        index1 += 1

    while index2 <= end:
        a[k] = temp[index2]
        k += 1
        index2 += 1


merge_sort(1, n)
print(result)
