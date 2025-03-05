## DFS, BackTracking
import sys
input = sys.stdin.readline

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
arr = []

def dfs(cnt, temp, stack):
    global result
    if cnt == 3:
        result = max(temp, result)
        return
    for i, j in stack:
        for ci, cj in dir:
            if 0 <= i + ci < n and 0 <= j + cj < m and not visited[i + ci][j + cj]:
                visited[i + ci][j + cj] = True
                dfs(cnt + 1, temp + arr[i + ci][j + cj], stack + [(i + ci, j + cj)])
                visited[i + ci][j + cj] = False ## BackTracking


for _ in range(n):
    arr.append(list(map(int, input().split())))

result = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(0, arr[i][j], [(i, j)])
        
print(result)