N = int(input())
dp = [0, 1]

if N < 2:
    print(dp[N])
else:
    for i in range(N - 1):
        dp.append(dp[-1] + dp[-2])
    print(dp[-1])