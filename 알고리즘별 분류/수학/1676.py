import sys
input = sys.stdin.readline

n = int(input())
fac = 1
for i in range(1, n + 1):
    fac *= i

fac = str(fac)
result = 0

for i in range(len(fac) - 1, -1, -1):
    if fac[i] == '0':
        result += 1
    else:
        print(result)
        break