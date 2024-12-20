from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
pair = int(input())
network = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(pair):
    a, b = map(int, input().split())
    network[a - 1].append(b - 1)
    network[b - 1].append(a - 1)

stack = deque([0])
while stack:
    network_num = stack.popleft()
    visited[network_num] = True
    for num in network[network_num]:
        if visited[num] == False:
            stack.append(num)

print(visited.count(True) - 1)