from collections import deque
import sys
input = sys.stdin.readline

P = int(input())
result = []
for _ in range(P):
    temp = 0
    line = deque(list(map(int, input().split())))
    line.popleft()
    temp_line = [line.popleft()]
    while line:
        now = line.popleft()
        for i, num in enumerate(temp_line):
            if now < num:
                temp += len(temp_line) - i
                temp_line.insert(i, now)
                now = 0
                break
        if now:
            temp_line.append(now)
    result.append(temp)

for i, num in enumerate(result):
    print(i + 1, num)