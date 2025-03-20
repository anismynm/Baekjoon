import heapq, math
N, K = map(int, input().split())

inf = int(1e9)
distance = [inf for _ in range(2 * max(N, K) - min(N, K) + 1)]
distance[N] = 0
visitQ = []
heapq.heappush(visitQ, (0, N))

while visitQ:
    dist, node = heapq.heappop(visitQ)
    if distance[node] < dist:
        continue
    if 2 * node < len(distance) and distance[2 * node] > dist:
        distance[2 * node] = dist
        heapq.heappush(visitQ, (dist, 2 * node))
    if node + 1 < len(distance) and distance[node + 1] > dist + 1:
        distance[node + 1] = dist + 1
        heapq.heappush(visitQ, (dist + 1, node + 1))
    if node > 0 and distance[node - 1] > dist + 1:
        distance[node - 1] = dist + 1
        heapq.heappush(visitQ, (dist + 1, node - 1))

print(distance[K])