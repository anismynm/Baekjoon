import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    if n == 1:
        result.append(max(sticker[0][0], sticker[1][0]))
        continue
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[0][1] + sticker[1][0]
    dp[1][1] = sticker[1][1] + sticker[0][0]
    for i in range(2, n):
        dp[0][i] = sticker[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = sticker[1][i] + max(dp[0][i - 1], dp[0][i - 2])
    result.append(max(dp[0][-1], dp[1][-1]))

for num in result:
    print(num)