import math, heapq, sys
input = sys.stdin.readline
GOLD = 10**14
SILVER = 10**7
BRONZE = 1

N, K = map(int, input().split())
rank = []
heapq.heapify(rank)

for _ in range(N):
    nation, gold, silver, bronze = map(int, input().split())
    if gold == 0 and silver == 0 and bronze == 0:
        heapq.heappush(rank, (-1, nation))
    else:
        heapq.heappush(rank, (math.log10(gold * GOLD + silver * SILVER + bronze * BRONZE), nation))

print(rank)