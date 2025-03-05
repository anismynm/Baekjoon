import sys
input = sys.stdin.readline

N = int(input())
graph = []
result = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    stack = []
    for p in range(N):
        if graph[i][p] == 1:
            stack.append(p)
    while stack:
        num = stack.pop()
        result[i][num] = 1
        for j in range(N):
            if graph[num][j] == 1 and result[i][j] != 1:
                result[i][j] = 1
                if i != num:
                    stack.append(j)

for i in range(N):
    for j in range(N):
        print(result[i][j], end = ' ')
    print()           