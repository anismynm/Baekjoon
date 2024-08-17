N, M = map(int, input().split())
basket = []
for i in range(N):
    basket.append('0')
for j in range(M):
    a, b, c = map(int, input().split())
    for k in range(a-1, b):
        basket[k] = c

print(' '.join(map(str, basket)))