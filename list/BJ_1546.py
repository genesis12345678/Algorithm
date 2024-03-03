n = int(input())
myList = list(map(int, input().split()))
myMax = max(myList)
mySum = sum(myList)

print(mySum * 100 / myMax / n)


