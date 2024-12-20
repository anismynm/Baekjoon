from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
tanghulu = list(map(int, input().split()))
pool = set(tanghulu)
result = 0

if len(pool) < 3:
    print(len(tanghulu))
    exit()

for iter in combinations(pool, 2):
    temp = 0
    for fruit in tanghulu:
        if fruit in iter:
            temp += 1
        else:
            if temp > result:
                result = temp
            temp = 0
    if temp > result:
        result = temp

print(result)