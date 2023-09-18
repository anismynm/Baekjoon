N, M = map(int, input().split())
basket = []
for i in range(N):
    basket.append(i+1)

for j in range(M):
    a, b = map(int, input().split())
    reverse_value = basket[a-1:b]
    reverse_value.reverse()
    basket = basket[:a-1] + reverse_value + basket[b:]

print(' '.join(map(str, basket)))
