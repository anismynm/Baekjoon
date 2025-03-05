from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
field = []
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    field.append(list(input().rstrip()))

result = 10000
stack = deque([(0, 0, 1)])
visited[0][0] = 1
while stack:
    i, j, temp = stack.popleft()
    if i == N - 1 and j == M - 1 and temp < result:
        result = temp
    for ni, nj in dir:
        if 0 <= i + ni < N and 0 <= j + nj < M and field[i + ni][j + nj] == '1' and not visited[i + ni][j + nj]:
            stack.append((i + ni, j + nj, temp + 1))
            visited[i + ni][j + nj] = 1
print(result)

## DFS
# def dfs(i, j, visited, temp):
#     global result
#     if i == N - 1 and j == M - 1 and temp < result:
#         result = temp
#         visited[i][j] = 0
#         return
#     for ni, nj in dir:
#         if 0 <= i + ni < N and 0 <= j + nj < M and field[i + ni][j + nj] == '1' and not visited[i + ni][j + nj]:
#             visited[i + ni][j + nj] = 1
#             dfs(i + ni, j + nj, visited, temp + 1)

# dfs(0, 0, visited, 1)