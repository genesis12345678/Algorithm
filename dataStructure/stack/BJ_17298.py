n = int(input())
a = list(map(int, input().split()))
result = [0] * n
myStack = []

for i in range(n):
    while myStack and a[i] > a[myStack[-1]]:  # 스택이 비어있지 않으면서, 들어올 값과 스택의 top에 있는 값을 비교
        # 새로 들어올 값이 더 크다면 스택 구조상 오큰수가 된다.
        result[myStack.pop()] = a[i]  # top 인덱스에 오큰수는 새로 들어올 값이 된다.
    myStack.append(i)  # 값이 아닌 index를 push한다.

while myStack:
    result[myStack.pop()] = -1

ans = []

for i in range(n):
    ans.append(str(result[i]))

print(" ".join(ans))
