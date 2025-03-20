import heapq, sys
input = sys.stdin.readline

N = int(input())
M = int(input())
inf = int(1e9)
graph = [[] for _ in range(N)]
distance = [inf for _ in range(N)]

for _ in range(M):
    i, j, cost = map(int, input().split())
    graph[i - 1].append((j - 1, cost))

start, end = map(int, input().split())
start -= 1
end -= 1

distance[start] = 0
visitQ = []
heapq.heappush(visitQ, (0, start))

while visitQ:
    dist, node = heapq.heappop(visitQ)
    if distance[node] < dist:
        continue
    for togo, cost in graph[node]:
        temp = distance[node] + cost
        if temp < distance[togo]:
            distance[togo] = temp
            heapq.heappush(visitQ, (temp, togo))

print(distance[end])