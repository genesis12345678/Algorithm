import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

treeSize = 1

while pow(2, treeSize) < n:  # 2^k >= n 을 만족하는 k의 최솟값 구하기 (k = treeSize)
    treeSize += 1

tree = [0] * (pow(2, treeSize) * 2)  # 2^k * 2의 크기로 tree 리스트 생성

leftNodeStartIndex = pow(2, treeSize)  # 2^k이 리프 노드의 시작 인덱스

for i in range(leftNodeStartIndex, leftNodeStartIndex + n):  # 초기 리프 노드 값 세팅
    tree[i] = int(input())


# 리프 노드 값을 바탕으로 부모 노드 값 한 자리씩 채우는 함수
def setTree(i):
    while i != 0:
        tree[i // 2] += tree[i]
        i -= 1


setTree(len(tree) - 1)


# index의 값을 value로 변경
def changeValue(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] += diff
        index //= 2  # /2로 부모 노드로 이동 하면서 값을 변경


# s ~ e 구간 합 구하는 함수
def getSum(s, e):
    partSum = 0

    while s <= e:
        if s % 2 == 1:  # start_index % 2 == 1이면 오른쪽 자식 이므로 단독 노드로 취급
            partSum += tree[s]
            s += 1
        if e % 2 == 0:  # end_index % 2 == 0이면 왼쪽 자식 이므로 단독 노드로 취급
            partSum += tree[e]
            e -= 1

        s //= 2  # 부모 노드 이동
        e //= 2  # 부모 노드 이동

    return partSum


result = []
for _ in range(m + k):
    q, s, e = map(int, input().split())
    if q == 1:
        changeValue(s + leftNodeStartIndex - 1, e)
    else:
        # 리프 노드의 인덱스로 맞추기 위해 '질의 인덱스 + 2^k - 1'로 변경 후 함수 실행
        s = s + leftNodeStartIndex - 1
        e = e + leftNodeStartIndex - 1

        result.append(str(getSum(s, e)))

print("\n".join(result))
