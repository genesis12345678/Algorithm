import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))


def swap(i, j):
    global a
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def quickSort(start, end, k):
    global a
    if start < end:
        pivot = partition(start, end)  # 중간 위치 피벗 설정
        if pivot == k:   # k번째 수가 피벗이면 더는 구할 필요 없음
            return
        elif pivot > k:  # k가 피벗보다 작으면 왼쪽 그룹만 정렬
            quickSort(start, pivot - 1, k)
        else:            # k가 피벗보다 크면 오른쪽 그룹만 정렬
            quickSort(pivot + 1, end, k)


def partition(start, end):
    global a

    if start + 1 == end:  # 데이터가 2개인 경우는 바로 비교하여 정렬
        if a[start] > a[end]:
            swap(start, end)
        return end

    m = (start + end) // 2  # 중간 index 구하기
    swap(start, m)  # start와 중간 swap
    pivot = a[start]  # pivot 값 지정
    i = start + 1  # start 지정
    j = end  # end 지정

    while i <= j:
        while pivot < a[j] and j > 0:  # 피벗보다 작은 값이 나올 때까지, 리스트 범위를 벗어나지 않을 때까지
            j -= 1  # end 왼쪽 이동
        while pivot > a[i] and i < len(a) - 1:  # 피벗보다
            i += 1

        if i <= j:  # i와 j의 위치가 다르면 swap하고 각각 안쪽으로 한 칸 이동
            swap(i, j)
            i += 1
            j -= 1

    #  i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    a[start] = a[j]  # 현재 피벗의 값을 j 위치로 이동
    a[j] = pivot  # 피벗 값을 나뉜 두 그룹의 경계 index에 저장
    return j  # 반환하는 j의 순서는 정해졌다.


quickSort(0, n - 1, k - 1)
print(a[k - 1])
