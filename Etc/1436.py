import sys
input = sys.stdin.readline

n = int(input())
num = 1
i = 0

while num < n:
    num += num * 9 + 9 * 10 ** i
    i += 1

print(num)
print(i + 3) # 이거 자릿수