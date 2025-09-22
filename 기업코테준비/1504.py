import heapq
import sys
input = sys.stdin.readline
INF = int(1e11)

N, E = map(int, input().split())
graph = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

u, v = map(int, input().split())

## 1~u+v~N, 1~v+u~N cost 비교
def djikstra(start, end):
    start -= 1
    end -= 1
    dist = [INF for _ in range(N)]
    dist[start] = 0
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (dist[start], start))
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        if dist[cur_node] < cur_cost:
            continue
        for i, cost in enumerate(graph[cur_node]):
            temp = cur_cost + cost
            if temp < dist[i]:
                dist[i] = temp
                heapq.heappush(heap, (dist[i], i))
    return dist[end]

result = min(djikstra(1, u) + djikstra(u, v) + djikstra(v, N), djikstra(1, v) + djikstra(v, u) + djikstra(u, N))

print(result) if result < INF else print(-1)