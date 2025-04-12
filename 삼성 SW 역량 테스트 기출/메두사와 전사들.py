import copy

N, M = map(int, input().split()) # 마을의 크기, 전사의 수
si, sj, ei, ej = map(int, input().split()) # 집 위치 ij, 공원 위치 ij
knight_pos = list(map(int, input().split())) # 전사 좌표

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
direction_lr = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 좌우상하
laser_direction = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # 북서, 북동, 남서, 남동
field = [] # 마을
knight_field = [[0 for _ in range(N)] for _ in range(N)] # 마을에서 전사의 위치

# knight_field 구축 -> 기사는 1, 빈 곳은 0
for i in range(M):
    knight_pos.append([knight_pos.pop(0), knight_pos.pop(0)])
for pos in knight_pos:
    knight_field[pos[0]][pos[1]] = 1

# field 입력
for _ in range(N):
    field.append(list(map(int, input().split())))

# field 최단 거리 기준으로 변환
stack = [(ei, ej)]
field_visited = [[0 for _ in range(N)] for _ in range(N)]
field_visited[ei][ej] = 1
while stack:
    i, j = stack.pop(0)
    for di, dj in direction:
        if 0 <= i + di < N and 0 <= j + dj < N and field_visited[i + di][j + dj] == 0:
            field_visited[i + di][j + dj] = 1
            if field[i + di][j + dj] == 0: # 도로
                field[i + di][j + dj] = field[i][j] + 1
                stack.append((i + di, j + dj))
            elif field[i + di][j + dj] == 1: # 비도로
                field[i + di][j + dj] = -1

if field[si][sj] == 0:
    print(-1)
    exit()
def laser_knight_cnt(d, pos): # d : 상하좌우 (0123)
    temp_knight_field = copy.deepcopy(knight_field)
    result = []
    start = -1
    end = N
    mid = True

    if d == 0: # 상
        for i in range(pos[0], -1, -1):
            # (1)
            if i != pos[0] and mid:
                if temp_knight_field[i][pos[1]] == 0: # 중간 점 찍기
                    temp_knight_field[i][pos[1]] = 2
                elif temp_knight_field[i][pos[1]] == 1:
                    temp_knight_field[i][pos[1]] = 2
                    result.append([i, pos[1]])
                    mid = False
            # (2)
            moving_i = i
            moving_j = pos[1]
            while True:
                moving_i += laser_direction[0][0]
                moving_j += laser_direction[0][1]
                if moving_i < 0 or moving_j == start:
                    break
                if temp_knight_field[moving_i][moving_j] == 0:
                    temp_knight_field[moving_i][moving_j] = 2
                elif temp_knight_field[moving_i][moving_j] == 1:
                    temp_knight_field[moving_i][moving_j] = 2
                    start = moving_j
                    result.append([moving_i, moving_j])
                    break
            # (3)
            moving_i = i
            moving_j = pos[1]
            while True:
                moving_i += laser_direction[1][0]
                moving_j += laser_direction[1][1]
                if moving_i < 0 or moving_j == end:
                    break
                if temp_knight_field[moving_i][moving_j] == 0:
                    temp_knight_field[moving_i][moving_j] = 2
                elif temp_knight_field[moving_i][moving_j] == 1:
                    temp_knight_field[moving_i][moving_j] = 2
                    end = moving_j
                    result.append([moving_i, moving_j])
                    break

    elif d == 1: # 하
        for i in range(pos[0], N):
            # (1)
            if i != pos[0] and mid:
                if temp_knight_field[i][pos[1]] == 0: # 중간 점 찍기
                    temp_knight_field[i][pos[1]] = 2
                elif temp_knight_field[i][pos[1]] == 1:
                    temp_knight_field[i][pos[1]] = 2
                    result.append([i, pos[1]])
                    mid = False
            # (2)
            moving_i = i
            moving_j = pos[1]
            while True:
                moving_i += laser_direction[2][0]
                moving_j += laser_direction[2][1]
                if moving_i >= N or moving_j == start:
                    break
                if temp_knight_field[moving_i][moving_j] == 0:
                    temp_knight_field[moving_i][moving_j] = 2
                elif temp_knight_field[moving_i][moving_j] == 1:
                    temp_knight_field[moving_i][moving_j] = 2
                    start = moving_j
                    result.append([moving_i, moving_j])
                    break
            # (3)
            moving_i = i
            moving_j = pos[1]
            while True:
                moving_i += laser_direction[3][0]
                moving_j += laser_direction[3][1]
                if moving_i >= N or moving_j == end:
                    break
                if temp_knight_field[moving_i][moving_j] == 0:
                    temp_knight_field[moving_i][moving_j] = 2
                elif temp_knight_field[moving_i][moving_j] == 1:
                    temp_knight_field[moving_i][moving_j] = 2
                    end = moving_j
                    result.append([moving_i, moving_j])
                    break

    elif d == 2: # 좌
        for j in range(pos[1], -1, -1):
            # (1)
            if j != pos[1] and mid:
                if temp_knight_field[pos[0]][j] == 0:
                    temp_knight_field[pos[0]][j] = 2
                elif temp_knight_field[pos[0]][j] == 1:
                    temp_knight_field[pos[0]][j] = 2
                    result.append([pos[0], j])
                    mid = False
            # (2)
            moving_i = pos[0]
            moving_j = j
            while True:
                moving_i += laser_direction[0][0]
                moving_j += laser_direction[0][1]
                if moving_i == start or moving_j < 0:
                    break
                if temp_knight_field[moving_i][moving_j] == 0:
                    temp_knight_field[moving_i][moving_j] = 2
                elif temp_knight_field[moving_i][moving_j] == 1:
                    temp_knight_field[moving_i][moving_j] = 2
                    start = moving_i
                    result.append([moving_i, moving_j])
                    break
            # (3)
            moving_i = pos[0]
            moving_j = j
            while True:
                moving_i += laser_direction[2][0]
                moving_j += laser_direction[2][1]
                if moving_i == end or moving_j < 0:
                    break
                if temp_knight_field[moving_i][moving_j] == 0:
                    temp_knight_field[moving_i][moving_j] = 2
                elif temp_knight_field[moving_i][moving_j] == 1:
                    temp_knight_field[moving_i][moving_j] = 2
                    end = moving_i
                    result.append([moving_i, moving_j])
                    break

    elif d == 3: # 우
        for j in range(pos[1], N):
            # (1)
            if j != pos[1] and mid:
                if temp_knight_field[pos[0]][j] == 0:
                    temp_knight_field[pos[0]][j] = 2
                elif temp_knight_field[pos[0]][j] == 1:
                    temp_knight_field[pos[0]][j] = 2
                    result.append([pos[0], j])
                    mid = False
            # (2)
            moving_i = pos[0]
            moving_j = j
            while True:
                moving_i += laser_direction[1][0]
                moving_j += laser_direction[1][1]
                if moving_i == start or moving_j >= N:
                    break
                if temp_knight_field[moving_i][moving_j] == 0:
                    temp_knight_field[moving_i][moving_j] = 2
                elif temp_knight_field[moving_i][moving_j] == 1:
                    temp_knight_field[moving_i][moving_j] = 2
                    start = moving_i
                    result.append([moving_i, moving_j])
                    break
            # (3)
            moving_i = pos[0]
            moving_j = j
            while True:
                moving_i += laser_direction[3][0]
                moving_j += laser_direction[3][1]
                if moving_i == end or moving_j >= N:
                    break
                if temp_knight_field[moving_i][moving_j] == 0:
                    temp_knight_field[moving_i][moving_j] = 2
                elif temp_knight_field[moving_i][moving_j] == 1:
                    temp_knight_field[moving_i][moving_j] = 2
                    end = moving_i
                    result.append([moving_i, moving_j])
                    break

    return temp_knight_field, result

# 각 턴 마다
current_pos = [si, sj]
# print('-- field --')
# for item in field:
#     print(item)
while True:
    knight_move = 0
    stone_knight = 0
    attack_knight = 0

    # 메두사의 이동
    to_go = -1 # 상하좌우 : 0123
    dist = field[current_pos[0]][current_pos[1]]
    for i, ij in enumerate(direction):
        if 0 <= current_pos[0] + ij[0] < N and 0 <= current_pos[1] + ij[1] < N: # 범위 내에 있고
            if field[current_pos[0] + ij[0]][current_pos[1] + ij[1]] != -1: # -1 아니고
                if field[current_pos[0] + ij[0]][current_pos[1] + ij[1]] != -2: # -2 아니고
                    if dist > field[current_pos[0] + ij[0]][current_pos[1] + ij[1]]: # 현재 최단 거리 보다 작으면
                        dist = field[current_pos[0] + ij[0]][current_pos[1] + ij[1]]
                        to_go = i

    # 공원에 도착
    if dist == 0:
        print(0)
        break

    # 메두사의 이동
    current_pos[0] += direction[to_go][0]
    current_pos[1] += direction[to_go][1]
    # print('(1) 메두사 이동 후 current_pos', current_pos)
    # 이동한 칸에 전사 있으면 전사 없앰
    for _ in range(len(knight_pos)):
        temp = knight_pos.pop(0)
        if current_pos == temp:
            continue
        else:
            knight_pos.append(temp)

    # knight_field 초기화
    knight_field = [[0 for _ in range(N)] for _ in range(N)]
    for pos in knight_pos:
        knight_field[pos[0]][pos[1]] = 1
    # print('knight_field')
    # for item in knight_field:
    #     print(item)
    # 메두사의 시선
    # 메두사 레이저 방향 정하기, 돌이 된 기사 count
    stone_knight_pos = []
    medusa_laser_dir = -1
    for d in range(4):
        a_temp_knight_field, pos_arr = laser_knight_cnt(d, current_pos)
        # print('방향 : ', d)
        # print('돌 되는 knight', pos_arr)
        # for item in a_temp_knight_field:
        #     print(item)
        temp_stone_knight = 0
        for pos in pos_arr:
            temp_stone_knight += knight_pos.count(pos)
        if temp_stone_knight > stone_knight:
            stone_knight = temp_stone_knight
            medusa_laser_dir = d

    # 설정된 방향대로 knight_field, stone_knight_pos 갱신
    knight_field, stone_knight_pos = laser_knight_cnt(medusa_laser_dir, current_pos)

    # 전사들의 이동
    # 메두사와의 최단거리 field 만들기
    dist_field = [[-1 for _ in range(N)] for _ in range(N)]
    stack = [current_pos]
    dist_field[current_pos[0]][current_pos[1]] = 0
    while stack:
        i, j = stack.pop(0)
        for di, dj in direction:
            if 0 <= i + di < N and 0 <= j + dj < N and dist_field[i + di][j + dj] == -1:
                stack.append([i + di, j + dj])
                dist_field[i + di][j + dj] = dist_field[i][j] + 1

    # print('(3) 전사 이동 전 knight_pos', knight_pos)
    for pos in knight_pos:
        if pos not in stone_knight_pos:
            dist = dist_field[pos[0]][pos[1]]
            temp_i = -1
            temp_j = -1
            for di, dj in direction:
                if 0 <= pos[0] + di < N and 0 <= pos[1] + dj < N and knight_field[pos[0] + di][pos[1] + dj] != 2 and dist > dist_field[pos[0] + di][pos[1] + dj]:
                    dist = dist_field[pos[0] + di][pos[1] + dj]
                    temp_i = di
                    temp_j = dj
            if temp_i == -1 and temp_j == -1: # 지금 있는 곳이 가장 최단거리
                continue
            knight_move += 1
            pos[0] += temp_i
            pos[1] += temp_j
            temp_i = -1
            temp_j = -1
            for di, dj in direction_lr:
                if 0 <= pos[0] + di < N and 0 <= pos[1] + dj < N and knight_field[pos[0] + di][pos[1] + dj] != 2 and dist > dist_field[pos[0] + di][pos[1] + dj]:
                    dist = dist_field[pos[0] + di][pos[1] + dj]
                    temp_i = di
                    temp_j = dj
            if temp_i == -1 and temp_j == -1: # 지금 있는 곳이 가장 최단거리
                continue
            knight_move += 1
            pos[0] += temp_i
            pos[1] += temp_j

    # print('(3) 전사 이동 후 knight_pos', knight_pos)
    # 전사의 공격
    for _ in range(len(knight_pos)):
        pos = knight_pos.pop(0)
        if current_pos == pos:
            attack_knight += 1
        else:
            knight_pos.append(pos)

    print(knight_move, stone_knight, attack_knight)