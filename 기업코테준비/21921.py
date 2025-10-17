N, X = map(int, input().split())
cnt = list(map(int, input().split()))
maxResult = 0
period = 1

prefixSum = [0]

for i in range(N):
    prefixSum.append(cnt[i] + prefixSum[-1])

for i in range(X, N + 1):
    if maxResult < prefixSum[i] - prefixSum[i - X]:
        maxResult = prefixSum[i] - prefixSum[i - X]
        period = 1
    elif maxResult == prefixSum[i] - prefixSum[i - X]:
        period += 1

if maxResult != 0:
    print(maxResult)
    print(period)
else:
    print("SAD")