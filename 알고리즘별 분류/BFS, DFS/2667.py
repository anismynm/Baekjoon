from collections import deque
import heapq
import sys
input = sys.stdin.readline

N = int(input())
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
apt = []
visited = [[0 for _ in range(N)] for _ in range(N)]
result = []
heapq.heapify(result)

def bfs(i, j):
    temp = 1
    stack = deque([(i, j)])
    while stack:
        ci, cj = stack.popleft()
        for ni, nj in dir:
            if 0 <= ci + ni < N and 0 <= cj + nj < N and not visited[ci + ni][cj + nj] and apt[ci + ni][cj + nj] == '1':
                stack.append((ci + ni, cj + nj))
                visited[ci + ni][cj + nj] = 1
                temp += 1
    heapq.heappush(result, temp)          

for _ in range(N):
    apt.append(list(input().rstrip()))

for i in range(N):
    for j in range(N):
        if not visited[i][j] and apt[i][j] == '1':
            visited[i][j] = 1
            bfs(i, j)

print(len(result))
while result:
    print(heapq.heappop(result))