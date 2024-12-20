from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))

pivot = 0
for elem in combinations(card, 3):
    result = sum(elem)
    if result == m:
        pivot = result
        break
    if pivot < result < m:
        pivot = result

print(pivot)