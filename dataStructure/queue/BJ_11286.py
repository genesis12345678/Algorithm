import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
myQueue = PriorityQueue()

result = []

for i in range(n):
    request = int(input())  # 요청 숫자
    if request == 0:  # 요청 숫자가 0이면
        if myQueue.empty():  # 큐가 비어있으면 0 출력
            result.append("0")
        else:  # 큐가 비어있지 않으면
            temp = myQueue.get()  # 튜플 get
            result.append(str((temp[1])))  # 절댓값이 아닌 request 값 출력
    else:
        myQueue.put((abs(request), request))

print("\n".join(result))
