N, M = map(int, input().split())
basket = []
for i in range(1, N+1):
    basket.append(i)
for j in range(M):
    a, b = map(int, input().split())
    basket[a-1], basket[b-1] = basket[b-1], basket[a-1]

print(' '.join(map(str, basket)))