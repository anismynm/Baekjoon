## 2025.03.23
## 30M

import sys
input = sys.stdin.readline

def bfs(i, j, visited):
    start_point = field[i][j]
    max_point = 0
    max_dist = 0
    stack = [(i, j, 0)]
    while stack:
        ci, cj, dist = stack.pop(0)
        for ni, nj in dir:
            if 0 <= ci + ni < N and 0 <= cj + nj < M and visited[ci + ni][cj + nj] == 0 and field[ci + ni][cj + nj] != 0:
                visited[ci + ni][cj + nj] = 1
                stack.append((ci + ni, cj + nj, dist + 1))
                if dist > max_dist or (dist == max_dist and start_point + field[ci + ni][cj + nj] > max_point):
                    max_dist = dist
                    max_point = start_point + field[ci + ni][cj + nj]
    return max_point, max_dist

N, M = map(int, input().split())
dir = [(0, -1), (1, 0), (-1, 0), (0, 1)]
max_point = 0
max_dist = 0
field = []

for i in range(N):
    field.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        if field[i][j] != 0:
            visited[i][j] = 1
            point, dist = bfs(i, j, visited)
            if dist > max_dist or (dist == max_dist and point > max_point):
                max_dist = dist
                max_point = point

print(max_point)