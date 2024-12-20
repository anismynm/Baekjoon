import sys
input = sys.stdin.readline

n = int(input())
i = 0

for temp in range(666, 2666800):
    if '666' in str(temp):
        i += 1
    if i == n:
        print(temp)
        break