## 2025.03.24
## 2H 21M

import copy
import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
field = []
cctv = [] # (cctv type, i, j)
result = int(1e9)

def up_laser(i, j, param):
    i -= 1
    while True:
        if i == -1 or param[i][j] == 6:
            break
        if 1 <= param[i][j] <= 5:
            i -= 1
            continue
        param[i][j] = -1
        i -= 1

def down_laser(i, j, param):
    i += 1
    while True:
        if i == N or param[i][j] == 6:
            break
        if 1 <= param[i][j] <= 5:
            i += 1
            continue
        param[i][j] = -1
        i += 1

def left_laser(i, j, param):
    j -= 1
    while True:
        if j == -1 or param[i][j] == 6:
            break
        if 1 <= param[i][j] <= 5:
            j -= 1
            continue
        param[i][j] = -1
        j -= 1

def right_laser(i, j, param):
    j += 1
    while True:
        if j == M or param[i][j] == 6:
            break
        if 1 <= param[i][j] <= 5:
            j += 1
            continue
        param[i][j] = -1
        j += 1

def dfs(k, stack, param):
    global result
    if k == len(stack):
        result = min(result, sum(row.count(0) for row in param))
        return

    typ, i, j = stack[k]
    if typ == 1:
        temp_param = copy.deepcopy(param)
        up_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

        temp_param = copy.deepcopy(param)
        right_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

        temp_param = copy.deepcopy(param)
        down_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

        temp_param = copy.deepcopy(param)
        left_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

    elif typ == 2:
        temp_param = copy.deepcopy(param)
        left_laser(i, j, temp_param)
        right_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

        temp_param = copy.deepcopy(param)
        up_laser(i, j, temp_param)
        down_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

    elif typ == 3:
        temp_param = copy.deepcopy(param)
        up_laser(i, j, temp_param)
        right_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

        temp_param = copy.deepcopy(param)
        right_laser(i, j, temp_param)
        down_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

        temp_param = copy.deepcopy(param)
        left_laser(i, j, temp_param)
        down_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

        temp_param = copy.deepcopy(param)
        left_laser(i, j, temp_param)
        up_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

    elif typ == 4:
        temp_param = copy.deepcopy(param)
        left_laser(i, j, temp_param)
        up_laser(i, j, temp_param)
        right_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

        temp_param = copy.deepcopy(param)
        up_laser(i, j, temp_param)
        right_laser(i, j, temp_param)
        down_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

        temp_param = copy.deepcopy(param)
        left_laser(i, j, temp_param)
        down_laser(i, j, temp_param)
        right_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)

        temp_param = copy.deepcopy(param)
        up_laser(i, j, temp_param)
        left_laser(i, j, temp_param)
        down_laser(i, j, temp_param)
        dfs(k + 1, stack, temp_param)
    else:
        print('ERROR')
        exit()

for i in range(N):
    temp = list(map(int, input().split()))
    for j, num in enumerate(temp):
        if 1 <= num <= 5:
            cctv.append((num, i, j))
    field.append(temp)

cctv = sorted(cctv, key = lambda x:x[0])
while cctv and cctv[-1][0] == 5:
    tp, i, j = cctv.pop()
    up_laser(i, j, field)
    down_laser(i, j, field)
    left_laser(i, j, field)
    right_laser(i, j, field)


dfs(0, cctv, field)
print(result)