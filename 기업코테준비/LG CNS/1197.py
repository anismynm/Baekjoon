import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = []
union_find = [i for i in range(V)]
result = 0
cnt = 0

def find(i):
    if union_find[i] != i:
        union_find[i] = find(union_find[i])
    return union_find[i]

def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    if v1 < v2:
        union_find[v2] = v1
    else:
        union_find[v1] = v2

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append((A - 1, B - 1, C))

graph = sorted(graph, key = lambda x:x[2])

for i in range(E):
    v1, v2, point = graph[i]
    if find(v1) != find(v2):
        union(v1, v2)
        result += point
        cnt += 1
        if cnt == V - 1:
            break
print(result)