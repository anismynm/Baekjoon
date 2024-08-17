from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
num = deque([])

for i in range(N):
    num.append(i + 1)

while (len(num) != 1):
    num.popleft()
    num.append(num.popleft())

print(num[0])