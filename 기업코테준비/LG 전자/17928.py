from collections import deque
N = int(input())
a = list(map(int, input().split()))
b = []
result = deque([])

while a:
    temp = a.pop()
    if b:
        while b and temp >= b[-1]:
            b.pop()
        if b:
            result.appendleft(b[-1])
        else:
            result.appendleft(-1)
    else:
        result.appendleft(-1)
    b.append(temp)

for num in result:
    print(num, end = ' ')
print()