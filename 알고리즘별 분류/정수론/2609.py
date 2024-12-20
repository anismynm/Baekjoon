import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

a, b = map(int,input().split())

max_num = max(a, b)
min_num = min(a, b)

result = []
while True:
    temp = gcd(max_num, min_num)
    if temp == 1:
        great = 1
        for i in result:
            great *= i
        print(great)
        print(great * max_num * min_num)
        break
    else:
        result.append(temp)
        max_num = max_num // temp
        min_num = min_num // temp