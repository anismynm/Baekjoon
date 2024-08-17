import sys
stacklist = []
result = 0

count = int(sys.stdin.readline())

for i in range(count):
    num = int(sys.stdin.readline())

    if (num == 0):
        stacklist.pop()
    else:
        stacklist.append(num)

print(sum(stacklist))