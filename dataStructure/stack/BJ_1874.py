n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(n):
    now = a[i]
    if now >= num:  # 현재 수열값 >= 오름차순 자연수: 값이 같아질 때까지 append(push) 수행
        while now >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:  # 현재 수열값 < 오름차순 자연수: pop을 수행해 수열 원소를 꺼냄
        pop = stack.pop()
        if pop > now:  # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없음
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)
