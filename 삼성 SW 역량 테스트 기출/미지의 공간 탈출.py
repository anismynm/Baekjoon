# ## 못품.
# ## 중간에 꼬이면 걍 끝. 신중히 코드 입력하기.
# ## 정확히 파악하면서 넘어가기. (확실하게)
import copy
N, M, F = map(int, input().split()) # field 크기, square 크기, time 크기
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동, 서, 남, 북
result = 0

field = [] # 2차원 배열 N * N
square = [] # [동, 서, 남, 북, 윗] 3차원 배열 5 * [M * M]
time = [] # (r, c, d, v) [0],[1] : 초기위치, [2] : 방향, [3] : 확산상수

square_visited = [[[0 for _ in range(M)] for _ in range(M)] for _ in range(5)]
field_visited = [[0 for _ in range(N)] for _ in range(N)]

square_start = (-1, -1, -1) # 입력받으면서
square_end = (-1, -1, -1)  # 2중 for문에서
field_start = (0, 0) # 2중 for문에서
square_idx = (-1, -1)
square_end_idx = (-1, -1)

for i in range(N):
    temp = list(map(int, input().split()))
    if 3 in temp and square_idx[0] == -1:
        square_idx = (i, temp.index(3))
        square_end_idx = (square_idx[0] + M, square_idx[1] + M)
    field.append(temp)

for i in range(square_idx[0], square_end_idx[0]):
    for j in range(square_idx[1], square_end_idx[1]):
        for k, item in enumerate(direction):
            if 0 <= i + item[0] < N - 1 and 0 <= j + item[1] < N - 1 and field[i + item[0]][j + item[1]] == 0:
                field_start = (i + item[0], j + item[1])
                if k == 0: # 동
                    square_end = (0, M - 1, square_end_idx[0] - 1 - i)
                elif k == 1: # 서
                    square_end = (1, M - 1, i - square_idx[0])
                elif k == 2: # 남
                    square_end = (2, M - 1, j - square_idx[1])
                elif k == 3: # 북
                    square_end = (3, M - 1, square_end_idx[1] - 1 - j)

for i in range(5):
    temp_arr = []
    for j in range(M):
        temp = list(map(int, input().split()))
        if 2 in temp:
            square_start = (i, j, temp.index(2))
        temp_arr.append(temp)
    square.append(temp_arr)

for _ in range(F):
    temp = list(map(int, input().split()))
    field[temp[0]][temp[1]] = 1
    time.append(temp)

# square BFS
stack = [(square_start[0], square_start[1], square_start[2], 0)]
square_visited[square_start[0]][square_start[1]][square_start[2]] = 1
while stack:
    d, i, j, cycle = stack.pop(0)
    if (d, i, j) == square_end:
        result = cycle
        break
    for di, dj in direction:
        if 0 <= i + di < M and 0 <= j + dj < M and square[d][i + di][j + dj] == 0 and square_visited[d][i + di][j + dj] == 0:
            stack.append((d, i + di, j + dj, cycle + 1))
            square_visited[d][i + di][j + dj] = 1

        elif i + di == -1: # 평면에서 위로
            if d == 0: # 동 -> 윗
                if square[4][M - 1 - j][M - 1] == 0 and square_visited[4][M - 1 - j][M - 1] == 0:
                    stack.append((4, M - 1 - j, M - 1, cycle + 1))
                    square_visited[4][M - 1 - j][M - 1] = 1
            elif d == 1: # 서 -> 윗
                if square[4][j][0] == 0 and square_visited[4][j][0] == 0:
                    stack.append((4, j, 0, cycle + 1))
                    square_visited[4][j][0] = 1
            elif d == 2: # 남 -> 윗
                if square[4][M - 1][j] == 0 and square_visited[4][M - 1][j] == 0:
                    stack.append((4, M - 1, j, cycle + 1))
                    square_visited[4][M - 1][j] = 1
            elif d == 3: # 북 -> 윗
                if square[4][0][M - 1 - j] == 0 and square_visited[4][0][M - 1 - j] == 0:
                    stack.append((4, 0, M - 1 - j, cycle + 1))
                    square_visited[4][0][M - 1 - j] = 1
            elif d == 4: # 윗 -> 북
                if square[3][0][M - 1 - j] == 0 and square_visited[3][0][M - 1 - j] == 0:
                    stack.append((3, 0, M - 1 - j, cycle + 1))
                    square_visited[3][0][M - 1 - j] = 1

        elif i + di == M: # 평면에서 아래로
            if d == 4: # 윗 -> 남
                if square[2][0][j] == 0 and square_visited[2][0][j] == 0:
                    stack.append((2, 0, j, cycle + 1))
                    square_visited[2][0][j] = 1

        elif j + dj == -1: # 평면에서 왼쪽으로
            if d == 0: # 동 -> 남
                if square[2][i][M - 1] == 0 and square_visited[2][i][M - 1] == 0:
                    stack.append((2, i, M - 1, cycle + 1))
                    square_visited[2][i][M - 1] = 1
            elif d == 1: # 서 -> 북
                if square[3][i][M - 1] == 0 and square_visited[3][i][M - 1] == 0:
                    stack.append((3, i, M - 1, cycle + 1))
                    square_visited[3][i][M - 1] = 1
            elif d == 2: # 남 -> 서
                if square[1][i][M - 1] == 0 and square_visited[1][i][M - 1] == 0:
                    stack.append((1, i, M - 1, cycle + 1))
                    square_visited[1][i][M - 1] = 1
            elif d == 3: # 북 -> 동
                if square[0][i][M - 1] == 0 and square_visited[0][i][M - 1] == 0:
                    stack.append((0, i, M - 1, cycle + 1))
                    square_visited[0][i][M - 1] = 1
            elif d == 4: # 윗 -> 서
                if square[1][0][i] == 0 and square_visited[1][0][i] == 0:
                    stack.append((1, 0, i, cycle + 1))
                    square_visited[1][0][i] = 1

        elif j + dj == M: # 평면에서 오른쪽으로
            if d == 0: # 동 -> 북
                if square[3][i][0] == 0 and square_visited[3][i][0] == 0:
                    stack.append((3, i, 0, cycle + 1))
                    square_visited[3][i][0] = 1
            elif d == 1: # 서 -> 남
                if square[2][i][0] == 0 and square_visited[2][i][0] == 0:
                    stack.append((2, i, 0, cycle + 1))
                    square_visited[2][i][0] = 1
            elif d == 2: # 남 -> 동
                if square[0][i][0] == 0 and square_visited[0][i][0] == 0:
                    stack.append((0, i, 0, cycle + 1))
                    square_visited[0][i][0] = 1
            elif d == 3: # 북 -> 서
                if square[1][i][0] == 0 and square_visited[1][i][0] == 0:
                    stack.append((1, i, 0, cycle + 1))
                    square_visited[1][i][0] = 1
            elif d == 4: # 윗 -> 동
                if square[0][0][M - 1 - i] == 0 and square_visited[0][0][M - 1 - i] == 0:
                    stack.append((0, 0, M - 1 - i, cycle + 1))
                    square_visited[0][0][M - 1 - i] = 1

if result == 0:
    print(-1)
    exit()
# F fix
result += 1
for items in time:
    for _ in range(result // items[3]):
        items[0] += direction[items[2]][0]
        items[1] += direction[items[2]][1]
        if 0 <= items[0] < N and 0 <= items[1] < N and field[items[0]][items[1]] == 0:
            field[items[0]][items[1]] = 5
        else:
            items[2] = -1
            break
# ------- SQUARE 완료, result = 9 -------
# 혹시라도 field 시작 하려는데 막힌 경우
clear = False
if field[field_start[0]][field_start[1]] == 1:
    print(-1)
    clear = True
if field[field_start[0]][field_start[1]] == 4:
    print(result)
    clear = True

# field BFS with F fix
temp_stack = [(field_start[0], field_start[1])]
field_visited[field_start[0]][field_start[1]] = 1
while not clear and temp_stack:
    stack = copy.deepcopy(temp_stack)
    result += 1
    for items in time:
        if items[2] != -1 and result % items[3] == 0:
            items[0] += direction[items[2]][0]
            items[1] += direction[items[2]][1]
            if 0 <= items[0] < N and 0 <= items[1] < N and field[items[0]][items[1]] == 0:
                field[items[0]][items[1]] = 5
            else:
                items[2] = -1
    temp_stack = []
    while stack:
        i, j = stack.pop(0)
        if field[i][j] == 4:
            print(result - 1)
            clear = True
            break
        for di, dj in direction:
            if 0 <= i + di < N and 0 <= j + dj < N and (field[i + di][j + dj] == 0 or field[i + di][j + dj] == 4) and field_visited[i + di][j + dj] == 0:
                temp_stack.append((i + di, j + dj))
                field_visited[i + di][j + dj] = 1

if not clear:
    print(-1)