from collections import deque
import sys
input = sys.stdin.readline

# 북 동 남 서
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
campus = deque([])

for i in range(N):
    campus.append(list(input()))
    campus[i].pop()
    if 'I' in campus[i]:
        x = i
        y = campus[i].index('I')

visited = [[False for _ in range(M)] for _ in range(N)]

# BFS
result = 0
stack = deque([(x, y)])
while stack:
    x, y = stack.popleft()
    if not visited[x][y]:
        visited[x][y] = True
        if campus[x][y] == 'P':
            result += 1
        for dx, dy in direction:
            tx = x + dx
            ty = y + dy
            if tx < 0 or tx > N - 1 or ty < 0 or ty > M - 1:
                continue
            if campus[tx][ty] == 'O' or campus[tx][ty] == 'P':
                stack.append((tx, ty))

if result:
    print(result)
else:
    print('TT')