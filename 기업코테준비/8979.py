import math, heapq, sys
input = sys.stdin.readline

N, K = map(int, input().split())
rank = []

for _ in range(N):
    nation, gold, silver, bronze = map(int, input().split())
    rank.append((gold, silver, bronze, nation))

rank = sorted(rank, key = lambda x:(x[0], x[1], x[2]), reverse = True)
if rank[0][3] == K:
    print(1)
else:
    result_rank = 0
    for i in range(1, N):
        if not (rank[i - 1][0] == rank[i][0] and rank[i - 1][1] == rank[i][1] and rank[i - 1][2] == rank[i][2]):
            result_rank = i + 1
        if rank[i][3] == K:
            print(result_rank)
            break