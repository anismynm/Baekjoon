from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
meet = []
for _ in range(n):
    meet.append(tuple(map(int, input().split())))

meet = sorted(meet, key = lambda x:(x[0], x[1]), reverse = True)
arr = deque([])
i = 0

while True:
    arr.appendleft(meet[i])
    temp_i = i
    for j in range(i + 1, n):
        if meet[j][1] <= meet[i][0]:
            i = j
            break
    if temp_i == i:
        break

print(meet)
print(len(arr))