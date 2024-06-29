import sys
input = sys.stdin.readline

nums = input().rstrip()
num = []
operator = []
temp = 0

# 입력 문자열 파싱
for elem in nums:
    if elem == '+' or elem == '-':
        operator.append(elem)
        num.append(temp)
        temp = 0
    else:
        if temp == 0:
            temp += int(elem)
        else:
            temp = 10 * temp + int(elem)
num.append(temp)

if operator.count('+') == len(operator):
    print(sum(num))
elif operator.count('-') == len(operator):
    for i in range(1, len(num)):
        num[i] = -1 * num[i]
    print(sum(num))
else:
    while operator.count('+') != 0:
        index = operator.index('+')
        num.insert(index, num.pop(index) + num.pop(index))
        operator.pop(index)
    for i in range(1, len(num)):
        num[i] = -1 * num[i]
    print(sum(num))