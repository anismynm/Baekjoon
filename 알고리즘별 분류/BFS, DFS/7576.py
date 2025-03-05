from collections import deque
import copy
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
tomato = []
stack = deque([])
temp_stack = deque([0])
day = -1

for i in range(N):
    row = list(map(int, input().split()))
    tomato.append(row)
    for j in range(M):
        if row[j] == 1:
            stack.append((i, j))

while temp_stack:
    temp_stack.clear()
    while stack:
        i, j = stack.popleft()
        for ni, nj in dir:
            if 0 <= i + ni < N and 0 <= j + nj < M and tomato[i + ni][j + nj] == 0:
                tomato[i + ni][j + nj] = 1
                temp_stack.append((i + ni, j + nj))
    day += 1
    stack = copy.deepcopy(temp_stack)

for row in tomato:
    if 0 in row:
        print(-1)
        exit()
print(day)