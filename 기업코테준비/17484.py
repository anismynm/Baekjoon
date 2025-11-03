import sys
input = sys.stdin.readline

inf = int(1e6)
direction = [(1, -1), (1, 0), (1, 1)]

N, M = map(int, input().split())
route = []
dp = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(3)]

for _ in range(N):
    route.append(list(map(int, input().split())))

for i in range(3):
    for j in range(M):
        dp[i][0][j] = route[0][j]

print(dp)