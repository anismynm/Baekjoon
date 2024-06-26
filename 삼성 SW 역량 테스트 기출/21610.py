from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
water = []
cloud = [[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]]
direction = []
distance = []

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(N):
    water.append(list(map(int, input().split())))

for _ in range(M):
    d, s = map(int, input().split())
    direction.append(d - 1)
    distance.append(s)

# 각 이동 시작
for i in range(M):
    visited = [[0] * N for _ in range(N)]
    # 모든 구름 옮기고 비 내리기
    for elem in cloud:
        elem[0] = (elem[0] + (distance[i] * dx[direction[i]])) % N
        elem[1] = (elem[1] + (distance[i] * dy[direction[i]])) % N
        water[elem[0]][elem[1]] += 1
        visited[elem[0]][elem[1]] = 1

    # 물복사버그
    for elem in cloud:
        for i in range(1, 8, 2):
            x = elem[0] + dx[i]
            y = elem[1] + dy[i]
            if (x < 0 or x >= N or y < 0 or y >= N):
                continue
            if (water[x][y] > 0):
                water[elem[0]][elem[1]] += 1
    
    cloud = []
    
    for i in range(N):
        for j in range(N):
            if (water[i][j] >= 2 and not visited[i][j]):
                cloud.append([i, j])
                water[i][j] -= 2

result = sum(sum(a) for a in water)
print(result)