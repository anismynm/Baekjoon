import sys
input = sys.stdin.readline

N, M = map(int, input().split())

candy = []
dp = [[0] * M] * N

for _ in range(N):
    candy.append(list(map(int, input().split())))

dp[0][0] = candy[0][0]

for i in range(N):
    for j in range(M):
        if i != 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + candy[i][j])
        if j != 0:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] + candy[i][j])
        if i != 0 and j != 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + candy[i][j])

print(dp[-1][-1])