import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
result = 0
dp = [0 for _ in range(N + 1)]
mod = [0 if i != 0 else 1 for i in range(M)]

for i in range(1, N + 1):
    dp[i] = dp[i - 1] + num[i - 1]
    mod[dp[i] % M] += 1

for i in mod:
    if i > 1:
        result += i * (i - 1) / 2

print(int(result))