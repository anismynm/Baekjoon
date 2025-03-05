from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
pic = []
visited = [[0 for _ in range(N)] for _ in range(N)]
result = [0, 0]

def bfs(i, j, color, pivot):
    stack = deque([(i, j)])
    while stack:
        i, j = stack.popleft()
        for ni, nj in dir:
            if 0 <= i + ni < N and 0 <= j + nj < N and not visited[i + ni][j + nj]:
                if pivot == 0:
                    if pic[i + ni][j + nj] == color:
                        visited[i + ni][j + nj] = 1
                        stack.append((i + ni, j + nj))
                else:
                    if color == 'B':
                        if pic[i + ni][j + nj] == color:
                            visited[i + ni][j + nj] = 1
                            stack.append((i + ni, j + nj))
                    else:
                        if pic[i + ni][j + nj] != 'B':
                            visited[i + ni][j + nj] = 1
                            stack.append((i + ni, j + nj))

for _ in range(N):
    pic.append(input().rstrip())

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j, pic[i][j], 0)
            result[0] += 1

visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j, pic[i][j], 1)
            result[1] += 1

print(result[0], result[1])