## 2025.03.20
## 45M
from collections import deque

N = int(input())
dir = deque([(0, 1), (1, 0), (0, -1), (-1, 0)]) # 우, 하, 좌, 상
tracking = deque([])
field = [[0 for _ in range(N)] for _ in range(N)]
field[0][0] = 1
dir_dict = {}

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    field[i - 1][j - 1] = 2

L = int(input())
for _ in range(L):
    sec, pos = input().split()
    dir_dict[int(sec)] = pos

snake_head = [0, 0]
snake_tail = [0, 0]
time = 0

while True:
    snake_head[0] += dir[0][0]
    snake_head[1] += dir[0][1]
    time += 1
    if snake_head[0] == -1 or snake_head[0] == N or snake_head[1] == -1 or snake_head[1] == N or field[snake_head[0]][snake_head[1]] == 1:
        print(time)
        break
    elif field[snake_head[0]][snake_head[1]] == 0:
        tracking.append((dir[0][0], dir[0][1]))
        field[snake_head[0]][snake_head[1]] = 1
        field[snake_tail[0]][snake_tail[1]] = 0
        tail_dir = tracking.popleft()
        snake_tail[0] += tail_dir[0]
        snake_tail[1] += tail_dir[1]
    elif field[snake_head[0]][snake_head[1]] == 2:
        tracking.append((dir[0][0], dir[0][1]))
        field[snake_head[0]][snake_head[1]] = 1
    if dir_dict.get(time):
        if dir_dict[time] == 'L':
            dir.rotate()
        else: # 'D'
            dir.rotate(-1)