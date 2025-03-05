from itertools import permutations
n, m = map(int, input().split())

for iter in permutations([i for i in range(1, n + 1)], m):
    for num in iter:
        print(num, end = ' ')
    print()