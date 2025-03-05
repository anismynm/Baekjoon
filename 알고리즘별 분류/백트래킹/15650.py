from itertools import combinations
N, M = map(int, input().split())
for iter in combinations([i for i in range(1, N + 1)], M):
    for num in iter:
        print(num, end = ' ')
    print()