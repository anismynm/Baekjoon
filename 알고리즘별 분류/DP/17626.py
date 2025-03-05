n = int(input())
dp = [0 if (i ** 0.5) % 1 or i == 0 else 1 for i in range(n + 1)]

for i in range(1, n + 1):
    if dp[i] != 0:
        continue
    j = 1
    while j * j <= i:
        if dp[i] == 0:
            dp[i] = dp[i - j * j] + dp[j * j]
        else:
            dp[i] = min(dp[i], dp[i - j * j] + dp[j * j])
        j += 1

print(dp[-1])