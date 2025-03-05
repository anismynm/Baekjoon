from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))

for iter in permutations(sorted(arr), M):
    for num in iter:
        print(num, end = ' ')
    print()