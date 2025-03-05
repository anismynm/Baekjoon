from collections import deque
import sys
input = sys.stdin.readline

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
visited = [[0 for _ in range(N)] for _ in range(M)]
field = []
white = 0
blue = 0

def bfs(i, j, pivot):
    global white
    global blue
    temp = 1
    stack = deque([(i, j)])
    while stack:
        ci, cj = stack.popleft()
        for ni, nj in dir:
            if 0 <= ci + ni < M and 0 <= cj + nj < N and not visited[ci + ni][cj + nj] and field[ci + ni][cj + nj] == pivot:
                stack.append((ci + ni, cj + nj))
                visited[ci + ni][cj + nj] = 1
                temp += 1
    if pivot == 'W':
        white += temp ** 2
    else:
        blue += temp ** 2

for _ in range(M):
    field.append(list(input().rstrip()))

for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        visited[i][j] = 1
        bfs(i, j, field[i][j])

print(white, blue)