from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = set()

for iter in permutations(sorted(arr), M):
    result.add(iter)

for iter in sorted(result):
    for num in iter:
        print(num, end = ' ')
    print()