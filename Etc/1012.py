import sys
input = sys.stdin.readline

t = int(input())
final = []

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if cx < 0 or cx >= n or cy < 0 or cy >= m or farm[cx][cy] == 0:
            continue
        farm[cx][cy] = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            stack.append((cx + dx, cy + dy))

for _ in range(t):
    farm = []
    result = 0
    m, n, k = map(int, input().split())
    for _ in range(n):
        farm.append([0] * m)

    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                dfs(i, j)
                result += 1
    final.append(result)

for i in final:
    print(i)