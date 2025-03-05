from collections import deque
import sys
input = sys.stdin.readline

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
field = []
result = [[-1 for _ in range(m)] for _ in range(n)]
start = (0, 0)
for i in range(n):
    temp = list(map(int, input().split()))
    field.append(temp)
    if 2 in temp:
        start = (i, temp.index(2))

stack = deque([start])
result[start[0]][start[1]] = 0
while stack:
    i, j = stack.popleft()
    for ni, nj in dir:
        if 0 <= i + ni < n and 0 <= j + nj < m and result[i + ni][j + nj] == -1:
            if field[i + ni][j + nj] == 0:
                result[i + ni][j + nj] = 0
            else:
                result[i + ni][j + nj] = result[i][j] + 1
                stack.append((i + ni, j + nj))

for i in range(n):
    for j in range(m):
        if result[i][j] == -1 and field[i][j] == 0:
            print(0, end = ' ')
        else:
            print(result[i][j], end = ' ')
    print()
