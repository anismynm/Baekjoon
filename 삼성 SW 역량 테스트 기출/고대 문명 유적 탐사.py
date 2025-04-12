# 3H 30M

K, M = map(int, input().split())
final = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
field = []
for _ in range(5):
    field.append(list(map(int, input().split())))

wall = list(map(int, input().split()))

def bfs(i, j, visited):
    result = 1
    stack = [(i, j)]
    while stack:
        ci, cj = stack.pop(0)
        for di, dj in direction:
            if 0 <= ci + di < 5 and 0 <= cj + dj < 5 and field[ci + di][cj + dj] == field[ci][cj] and not visited[ci + di][cj + dj]:
                stack.append((ci + di, cj + dj))
                visited[ci + di][cj + dj] = 1
                result += 1
    if result >= 3:
        return result
    else:
        return 0

def rotate(i, j): # 한 중심 좌표 기준에서 회전으로 나올 수 있는 가장 큰 가치, 회전각 리턴
    worth = -1
    angle = -1
    # 회전
    for r in range(3): # 0, 1, 2 : 90, 180, 270
        temp = list(map(list, zip(*field[i+1:i-2:-1])))[j-1:j+2] if i > 1 else list(map(list, zip(*field[i+1::-1])))[j-1:j+2]
        for p in range(-1, 2):
            for q in range(-1, 2):
                field[i + p][j + q] = temp[p + 1][q + 1]
        # BFS
        temp_worth = 0
        visited = [[0 for _ in range(5)] for _ in range(5)]
        for ii in range(5):
            for jj in range(5):
                if not visited[ii][jj]:
                    visited[ii][jj] = 1
                    temp_worth += bfs(ii, jj, visited)

        if temp_worth != 0 and temp_worth > worth:
            worth = temp_worth
            angle = r

    # 원 상태 복귀
    temp = list(map(list, zip(*field[i + 1:i - 2:-1])))[j - 1:j + 2] if i > 1 else list(map(list, zip(*field[i + 1::-1])))[j - 1:j + 2]
    for p in range(-1, 2):
        for q in range(-1, 2):
            field[i + p][j + q] = temp[p + 1][q + 1]

    return worth, angle

wall_num = 0
while K:
    worth = -1
    angle = -1
    center_i = -1
    center_j = -1
    for j in range(1, 4):
        for i in range(1, 4):
            temp_worth, temp_angle = rotate(i, j)
            if temp_worth > worth:
                worth = temp_worth
                angle = temp_angle
                center_i = i
                center_j = j
            elif temp_worth == worth and temp_angle < angle:
                worth = temp_worth
                angle = temp_angle
                center_i = i
                center_j = j
    if worth == -1:
        break

    for _ in range(angle + 1):
        temp = list(map(list, zip(*field[center_i + 1:center_i - 2:-1])))[center_j - 1:center_j + 2] if center_i > 1 else list(map(list, zip(*field[center_i + 1::-1])))[center_j - 1:center_j + 2]
        for p in range(-1, 2):
            for q in range(-1, 2):
                field[center_i + p][center_j + q] = temp[p + 1][q + 1]

    # 유물 획득, 연쇄 획득
    worth = 0
    while True:
        visited = [[0 for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if field[i][j] != 0 and not visited[i][j]:
                    visited[i][j] = 1
                    result_stack = [(i, j)]
                    stack = [(i, j)]
                    while stack:
                        ci, cj = stack.pop(0)
                        for di, dj in direction:
                            if 0 <= ci + di < 5 and 0 <= cj + dj < 5 and field[i][j] == field[ci + di][cj + dj] and not visited[ci + di][cj + dj]:
                                visited[ci + di][cj + dj] = 1
                                stack.append((ci + di, cj + dj))
                                result_stack.append((ci + di, cj + dj))
                    if len(result_stack) >= 3:
                        for p, q in result_stack:
                            field[p][q] = 0

        empty_cnt = sum(field[i].count(0) for i in range(5))
        worth += empty_cnt
        if empty_cnt == 0:
            break
        for j in range(5):
            for i in range(4, -1, -1):
                if field[i][j] == 0:
                    field[i][j] = wall[wall_num]
                    wall_num += 1
    if worth == 0:
        break
    final.append(worth)
    K -= 1

if final:
    for item in final:
        print(item, end = ' ')