t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0 for _ in range(n)]
    if n >= 1:
        dp[0] = 1
    if n >= 2:
        dp[1] = 1
    if n >= 3:
        dp[2] = 1
    for i in range(3, n):
        dp[i] = dp[i - 2] + dp[i - 3]
    print(dp[-1])