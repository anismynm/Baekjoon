from collections import deque
import copy
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
dir = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
tomato = []
stack = deque([])
temp_stack = deque([0])
day = -1

for i in range(H):
    layer = []
    for j in range(N):
        temp = list(map(int, input().split()))
        layer.append(temp)
        for k in range(M):
            if temp[k] == 1:
                stack.append((i, j, k))
    tomato.append(layer)

while temp_stack:
    temp_stack.clear()
    while stack:
        i, j, k = stack.popleft()
        for ni, nj, nk in dir:
            if 0 <= i + ni < H and 0 <= j + nj < N and 0 <= k + nk < M and tomato[i + ni][j + nj][k + nk] == 0:
                tomato[i + ni][j + nj][k + nk] = 1
                temp_stack.append((i + ni, j + nj, k + nk))
    day += 1
    stack = copy.deepcopy(temp_stack)

for layer in tomato:
    for row in layer:
        if 0 in row:
            print(-1)
            exit()
print(day)