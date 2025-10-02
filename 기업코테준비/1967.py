## 트리의 지름 : x -> y, y -> z 가장 먼 y, z
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = 0
idx = -1

def dfs(node, cost):
    global result, idx
    visited[node] = True
    if result < cost:
        result = cost
        idx = node
    for next_node, next_cost in tree[node]:
        if not visited[next_node]:
            dfs(next_node, next_cost + cost)


for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    tree[parent].append((child, cost))
    tree[child].append((parent, cost))

dfs(1, 0)
visited = [False] * (n + 1)
dfs(idx, 0)
print(result)