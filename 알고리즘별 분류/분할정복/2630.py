import sys
input = sys.stdin.readline

N = int(input())
paper = []
result = [0, 0]

def dfs(start, length):
    if length == 1:
        if paper[start[0]][start[1]] == 0:
            result[0] += 1
        else:
            result[1] += 1
        return
    mid = (start[0] + length // 2, start[1] + length // 2)
    part = (start, (start[0], mid[1]), (mid[0], start[1]), mid)
    for si, sj in part:
        size = sum([paper[i][j] for i in range(si, si + length // 2) for j in range(sj, sj + length // 2)])
        if size == 0:
            result[0] += 1
        elif size == length ** 2 // 4:
            result[1] += 1
        else:
            dfs((si, sj), length // 2)

for _ in range(N):
    paper.append(list(map(int, input().split())))

if sum(paper[i][j] for i in range(N) for j in range(N)) == 0:
    print(result[0] + 1)
    print(result[1])
elif sum(paper[i][j] for i in range(N) for j in range(N)) == N ** 2:
    print(result[0])
    print(result[1] + 1)
else:
    dfs((0, 0), N)
    print(result[0]) # white
    print(result[1]) # blue