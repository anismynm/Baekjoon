from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = int(1e9)
house = []
chicken = []
dist = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            house.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))

for hi, hj in house:
    temp = []
    for ci, cj in chicken:
        temp.append(abs(hi - ci) + abs(hj - cj))
    dist.append(temp)

for iter in combinations([i for i in range(len(chicken))], M):
    temp = 0
    for row in dist:
        temp += min([row[i] for i in iter])
    if temp < result:
        result = temp

print(result)