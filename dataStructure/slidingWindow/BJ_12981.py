checkList = [0] * 4
curList = [0] * 4
checkNum = 0


# 함수
def myAdd(c):  # 새로 들어온 문자를 처리하는 함수
    global checkList, curList, checkNum
    if c == 'A':
        curList[0] += 1
        if curList[0] == checkList[0]:
            checkNum += 1
    elif c == 'C':
        curList[1] += 1
        if curList[1] == checkList[1]:
            checkNum += 1
    elif c == 'G':
        curList[2] += 1
        if curList[2] == checkList[2]:
            checkNum += 1
    elif c == 'T':
        curList[3] += 1
        if curList[3] == checkList[3]:
            checkNum += 1


def myRemove(c):  # 제거되는 문자를 처리하는 함수
    global checkList, curList, checkNum
    if c == 'A':
        if curList[0] == checkList[0]:
            checkNum -= 1
        curList[0] -= 1
    elif c == 'C':
        if curList[1] == checkList[1]:
            checkNum -= 1
        curList[1] -= 1
    elif c == 'G':
        if curList[2] == checkList[2]:
            checkNum -= 1
        curList[2] -= 1
    elif c == 'T':
        if curList[3] == checkList[3]:
            checkNum -= 1
        curList[3] -= 1


s, p = map(int, input().split())
result = 0
a = list(input())
checkList = list(map(int, input().split()))

for i in range(4):  # 0이면 아무 조건 없이 조건에 만족한다.
    if checkList[i] == 0:
        checkNum += 1

for i in range(p):  # 초기 p 부분 문자열 처리 부분
    myAdd(a[i])

if checkNum == 4:  # 처음부터 비밀번호 조건을 만족할 수도 있다.
    result += 1

for i in range(p, s):
    j = i - p  # j = 첫 칸, i = 끝 칸

    # 인덱스(첫 번째가 0)를 기준으로 계산하면 추가될 칸과 지워질 칸이 나온다.
    # 초기 부분은 이미 해결했으니 그 다음 칸부터 해결하면 된다.
    myAdd(a[i])  # 추가될 칸(끝에서 다음 칸)
    myRemove(a[j])  # 지워킬 칸(처음보다 전 칸)

    if checkNum == 4:
        result += 1

print(result)
