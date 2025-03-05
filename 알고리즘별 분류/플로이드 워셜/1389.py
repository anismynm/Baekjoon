## 플로이드 워셜 - 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘
## D13 = min(D13, D1N + DN3) : 모든 N 순회, N를 거쳐가는거, 그냥 가는거 비교

import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd_warshall(a, b, k):
    if relation[a][b] > relation[a][k] + relation[k][b]:
        return relation[a][k] + relation[k][b]
    else:
        return relation[a][b]

N, M = map(int, input().split())
relation = [[0 if (i == j) else INF for i in range(N)] for j in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    relation[a - 1][b - 1] = 1
    relation[b - 1][a - 1] = 1

for k in range(N):
    for a in range(N):
        for b in range(N):
            relation[a][b] = floyd_warshall(a, b, k)

bacon = INF
result = 0

for i in range(N):
    if bacon > sum(relation[i]):
        bacon = sum(relation[i])
        result = i + 1

print(result)