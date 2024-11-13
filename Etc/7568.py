from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
info = []

for _ in range(N):
    w, h = map(int, input().split())
    info.append([w, h, 0])

for comb in combinations(info, 2):
    if comb[0][0] > comb[1][0]:
        if comb[0][1] > comb[1][1]:
            comb[1][2] += 1
        else:
            continue
    elif comb[0][0] < comb[1][0]:
        if comb[0][1] < comb[1][1]:
            comb[0][2] += 1
        else:
            continue
    else:
        continue

for elem in info:
    print(elem[2] + 1, end = ' ')
print()