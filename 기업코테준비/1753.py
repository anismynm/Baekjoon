import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
graph = [[] for _ in range(V)]
start = int(input())

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))

dist = [INF for _ in range(V)]
dist[start - 1] = 0
visitQ = []
heapq.heapify(visitQ)
heapq.heappush(visitQ, (dist[start-1], start - 1))
while visitQ:
    cur_cost, cur_node = heapq.heappop(visitQ)
    if dist[cur_node] < cur_cost:
        continue
    for node, cost in (graph[cur_node]):
        temp = cur_cost + cost
        if temp < dist[node]:
            dist[node] = temp
            heapq.heappush(visitQ, (dist[node], node))

for num in dist:
    if num == INF:
        print('INF')
    else:
        print(num)