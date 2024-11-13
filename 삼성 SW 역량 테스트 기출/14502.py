# Pypy3
# deepcopy -> 깊은복사 (2차원 배열)
# copy -> 단순 깊은복사 (1차원 배열)
from collections import deque
from itertools import combinations
import sys
from copy import copy, deepcopy
input = sys.stdin.readline

di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

N, M = map(int, input().split())

og_field = []
og_visited = [[False for _ in range(M)] for _ in range(N)]
og_virus_index = []
empty_index = []
result = 0

def bfs(arr, stack):
    stack = deque(stack)
    while stack:
        i, j = stack.popleft()
        if visited[i][j] == False:
            visited[i][j] = True
            for d in range(4):
                ci = i + di[d]
                cj = j + dj[d]
                if ci < 0 or ci >= N or cj < 0 or cj >= M:
                    continue
                else:
                    if arr[ci][cj] == 0:
                        arr[ci][cj] = 2
                        stack.append((ci, cj))

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 0:
            empty_index.append((i, j))
        elif temp[j] == 2:
            og_virus_index.append((i, j))
    og_field.append(temp)

for elem in combinations(empty_index, 3):
    field = deepcopy(og_field)
    visited = deepcopy(og_visited)
    virus_index = copy(og_virus_index)
    temp = 0

    for point in list(elem):
        i, j = point[0], point[1]
        field[i][j] = 1
    bfs(field, virus_index)

    for array in field:
        temp += array.count(0)
    if temp > result:
        result = temp

print(result)