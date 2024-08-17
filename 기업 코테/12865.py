import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [0]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split()))) # 무게, 가치

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if stuff[i][0] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], stuff[i][1] + dp[i - 1][j - stuff[i][0]])

print(dp[-1][-1])