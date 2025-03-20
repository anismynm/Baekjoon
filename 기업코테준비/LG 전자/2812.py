import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(int(d) for d in input().rstrip())

pivot = max(num[:K + 1])
K -= num.index(pivot)
num = num[num.index(pivot):]

i = 0
while K and i < len(num) - 1:
    if num[i] < num[i + 1]:
        num.pop(i)
        K -= 1
        i -= 1
    else:
        i += 1

if K:
    num = num[:len(num) - K]

for i in num:
    print(i, end = '')
print()