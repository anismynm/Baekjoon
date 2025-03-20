import sys
input = sys.stdin.readline

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for i in range(2, N):
    if field[0][i] == 0:
        dp[0][i][0] = dp[0][i - 1][0]

for i in range(1, N):
    for j in range(1, N):
        temp = [0, 0, 0]
        if field[i][j] == 0:
            temp[0] += dp[i][j - 1][0] + dp[i][j - 1][2]
            temp[1] += dp[i - 1][j][1] + dp[i - 1][j][2]
            if field[i - 1][j] == 0 and field[i][j - 1] == 0:
                temp[2] += sum(dp[i - 1][j - 1]) # blue
        dp[i][j] = temp

print(sum(dp[-1][-1]))