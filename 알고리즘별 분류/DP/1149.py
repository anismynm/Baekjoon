import sys
input = sys.stdin.readline

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

dp = [cost[0]]
for i in range(1, N):
    dp.append([0, 0, 0])
    for j in range(3):
        dp[i][j] = cost[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])

print(min(dp[-1]))