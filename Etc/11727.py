import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 3
    else:
        dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[-1] % 10007)