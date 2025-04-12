## 2025.03.20
## 27M 틀
## 30M
from collections import deque

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, L, R = map(int, input().split())

def bfs(i, j, nation, visited, tag):
    population = 0
    nation_cnt = 0
    stack = deque([(i, j)])
    while stack:
        ci, cj = stack.popleft()
        population += nation[ci][cj]
        nation_cnt += 1
        for ni, nj in dir:
            if 0 <= ci + ni < N and 0 <= cj + nj < N and visited[ci + ni][cj + nj] == -1 and L <= abs(nation[ci][cj] - nation[ci + ni][cj + nj]) <= R:
                visited[ci + ni][cj + nj] = tag
                stack.append((ci + ni, cj + nj))
    return population // nation_cnt

day = 0
nation = []
for _ in range(N):
    nation.append(list(map(int, input().split())))

while True:
    tag = 0
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    nation_pop = []

    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                visited[i][j] = tag
                nation_pop.append(bfs(i, j, nation, visited, tag))
                tag += 1

    if len(nation_pop) == N**2:
        print(day)
        break
    else:
        for i in range(N):
            for j in range(N):
                nation[i][j] = nation_pop[visited[i][j]]
    day += 1