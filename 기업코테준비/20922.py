import sys
input = sys.stdin.readline

N, K = map(int, input().split())

num = list(map(int, input().split()))
cnt = [0] * 100001
cnt[num[0]] += 1

end = 0
result = 1

for start in range(N):
    while end < N - 1 and cnt[num[end]] <= K:
        end += 1
        cnt[num[end]] += 1
        if end == N - 1 and cnt[num[end]] <= K:
            result = max(result, end - start + 1)
    result = max(result, end - start)
    cnt[num[start]] -= 1

print(result)