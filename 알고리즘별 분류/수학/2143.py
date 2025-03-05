import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a_dp = {}
b_dp = {}
result = 0

for i in range(n):
    a_dp[a[i]] = 1 if a[i] not in a_dp else a_dp[a[i]] + 1
    a_temp = a[i]
    for j in range(i + 1, n):
        a_temp += a[j]
        a_dp[a_temp] = 1 if a_temp not in a_dp else a_dp[a_temp] + 1

for i in range(m):
    b_dp[b[i]] = 1 if b[i] not in b_dp else b_dp[b[i]] + 1
    b_temp = b[i]
    for j in range(i + 1, m):
        b_temp += b[j]
        b_dp[b_temp] = 1 if b_temp not in b_dp else b_dp[b_temp] + 1

for key, value in a_dp.items():
    try:
        result += b_dp[T - key] * value
    except:
        continue

print(result)