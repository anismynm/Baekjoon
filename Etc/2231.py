import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    temp = i + sum(int(j) for j in str(i))
    if temp == n:
        print(i)
        break
else:
    print(0)