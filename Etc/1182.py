from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
result = 0

for i in range(1, n + 1):
    for elem in combinations(num_list, i):
        if sum(elem) == s:
            result += 1

print(result)