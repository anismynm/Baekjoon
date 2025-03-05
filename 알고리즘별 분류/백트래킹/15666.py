from itertools import combinations_with_replacement
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = set()

for iter in combinations_with_replacement(sorted(arr), M):
    result.add(iter)

for iter in sorted(result):
    for num in iter:
        print(num, end = ' ')
    print()