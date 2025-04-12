## 2025.03.21
## 50M 시간 초과
## 57M 시간 초과
## 1H 5M pypy3

import sys
from collections import deque
input = sys.stdin.readline

R, C, T = map(int, input().split())
dir = deque([(0, 1), (-1, 0), (0, -1), (1, 0)])
field = []
cleaner = [] # [2, 3]

for i in range(R):
    temp = list(map(int, input().split()))
    if not cleaner and temp[0] == -1:
        cleaner = [i, i + 1]
    field.append(temp)

while T:
    # 미세먼지 확산 (BFS)
    stack = []
    for i in range(R):
        for j in range(C):
            if field[i][j] != 0 and field[i][j] != -1:
                stack.append((i, j, field[i][j] // 5))
    while stack:
        i, j, spr = stack.pop(0)
        cnt = 0
        for di, dj in dir:
            if 0 <= i + di < R and 0 <= j + dj < C and field[i + di][j + dj] != -1:
                field[i + di][j + dj] += spr
                cnt += 1
        field[i][j] -= spr * cnt

    temp = 0
    pos = [cleaner[0], 1]
    while True:
        if pos == [cleaner[0], 0]:
            dir.rotate(-1)
            break
        field[pos[0]][pos[1]], temp = temp, field[pos[0]][pos[1]]
        if pos == [cleaner[0], C - 1] or pos == [0, C - 1] or pos == [0, 0] or pos == [cleaner[0], 0]:
            dir.rotate(-1)
        pos[0] += dir[0][0]
        pos[1] += dir[0][1]

    temp = 0
    pos = [cleaner[1], 1]
    while True:
        if pos == [cleaner[1], 0]:
            dir.rotate()
            break
        field[pos[0]][pos[1]], temp = temp, field[pos[0]][pos[1]]
        if pos == [cleaner[1], C - 1] or pos == [R - 1, C - 1] or pos == [R - 1, 0] or pos == [cleaner[1], 0]:
            dir.rotate()
        pos[0] += dir[0][0]
        pos[1] += dir[0][1]
    # 시간 감소
    T -= 1

print(sum([sum(row) for row in field]) + 2)