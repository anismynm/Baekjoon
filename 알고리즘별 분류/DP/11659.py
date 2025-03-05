import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = nums[0]

for i in range(1, N):
    dp[i] = dp[i - 1] + nums[i]

for _ in range(M):
    start, end = map(int, input().split())
    print(dp[end - 1] - dp[start - 2] if start > 1 else dp[end - 1])