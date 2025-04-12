import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T + 1):
    length = int(input())
    graph = list(map(int, input().split()))
    result = 0
    while graph:
        max_idx = graph.index(max(graph))
        left_graph = graph[:max_idx + 1]
        result += left_graph[-1] * (len(left_graph) - 1) - sum(left_graph[:-1])
        graph = graph[max_idx + 1:]
    print(f'#{i} {result}')