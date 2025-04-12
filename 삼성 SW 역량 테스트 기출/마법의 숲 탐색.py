# 2H 5M
# 종이에 일단 다 생각을 해두고
R, C, K = map(int, input().split()) # 6행 5열, 정령 6개
golem = []
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 남, 북, 동, 서
field = [[0 for _ in range(C)] for _ in range(R)]
result = 0

for _ in range(K):
    c, d = map(int, input().split())
    golem.append((c - 1, d))

golem_num = 1
while golem:
    a, d = golem.pop(0) # center = 1, exit = 3
    center = [-2, a] # [-2, 1]

    while center[0] < R - 2:
        if center[0] == -2:
            if field[center[0] + 2][center[1]] == 0:
                center[0] += 1
                continue
            elif center[1] > 1 and field[center[0] + 2][center[1] - 1] == 0:
                center[0] += 1
                center[1] -= 1
                d = (d - 1) % 4
                continue
            elif center[1] < C - 2 and field[center[0] + 2][center[1] + 1] == 0:
                center[0] += 1
                center[1] += 1
                d = (d + 1) % 4
                continue

        elif center[0] == -1:
            if field[center[0] + 1][center[1] - 1] == 0 and field[center[0] + 1][center[1] + 1] == 0 and field[center[0] + 2][center[1]] == 0:
                center[0] += 1
                continue
            elif center[1] > 1 and field[center[0] + 1][center[1] - 2] == 0 and field[center[0] + 1][center[1] - 1] == 0 and field[center[0] + 2][center[1] - 1] == 0:
                center[0] += 1
                center[1] -= 1
                d = (d - 1) % 4
                continue
            elif center[1] < C - 2 and field[center[0] + 2][center[1] + 1] == 0 and field[center[0] + 1][center[1] + 1] == 0 and field[center[0] + 1][center[1] + 2] == 0:
                center[0] += 1
                center[1] += 1
                d = (d + 1) % 4
                continue

        elif center[0] == 0:
            if field[center[0] + 1][center[1] - 1] == 0 and field[center[0] + 1][center[1] + 1] == 0 and field[center[0] + 2][center[1]] == 0:
                center[0] += 1
                continue
            elif center[1] > 1 and field[center[0] + 1][center[1] - 2] == 0 and field[center[0] + 1][center[1] - 1] == 0 and field[center[0] + 2][center[1] - 1] == 0 and field[center[0]][center[1] - 2] == 0:
                center[0] += 1
                center[1] -= 1
                d = (d - 1) % 4
                continue
            elif center[1] < C - 2 and field[center[0] + 2][center[1] + 1] == 0 and field[center[0] + 1][center[1] + 1] == 0 and field[center[0] + 1][center[1] + 2] == 0 and field[center[0]][center[1] + 2] == 0:
                center[0] += 1
                center[1] += 1
                d = (d + 1) % 4
                continue

        else: # > 0
            if field[center[0] + 1][center[1] - 1] == 0 and field[center[0] + 1][center[1] + 1] == 0 and field[center[0] + 2][center[1]] == 0:
                center[0] += 1
                continue
            elif center[1] > 1 and field[center[0] + 1][center[1] - 2] == 0 and field[center[0] + 1][center[1] - 1] == 0 and field[center[0] + 2][center[1] - 1] == 0 and field[center[0]][center[1] - 2] == 0 and field[center[0] - 1][center[1] - 1] == 0:
                center[0] += 1
                center[1] -= 1
                d = (d - 1) % 4
                continue
            elif center[1] < C - 2 and field[center[0] + 2][center[1] + 1] == 0 and field[center[0] + 1][center[1] + 1] == 0 and field[center[0] + 1][center[1] + 2] == 0 and field[center[0]][center[1] + 2] == 0 and field[center[0] - 1][center[1] + 1] == 0:
                center[0] += 1
                center[1] += 1
                d = (d + 1) % 4
                continue
        break

    if center[0] < 1:
        field = [[0 for _ in range(C)] for _ in range(R)]
        golem_num = 1
        continue

    field[center[0]][center[1]] = golem_num
    field[center[0] + 1][center[1]] = -golem_num if d == 2 else golem_num
    field[center[0] - 1][center[1]] = -golem_num if d == 0 else golem_num
    field[center[0]][center[1] + 1] = -golem_num if d == 1 else golem_num
    field[center[0]][center[1] - 1] = -golem_num if d == 3 else golem_num

    # test
    # print(center)
    # for item in field:
    #     print(item)

    # 정령을 위한 BFS 시작
    visited = [[0 for _ in range(C)] for _ in range(R)]
    southest = 0
    stack = [center]
    visited[center[0]][center[1]] = 1
    while stack:
        i, j = stack.pop(0)
        if i > southest:
            southest = i
        if field[i][j] > 0: # 현재 위치가 출구가 아님
            for ci, cj in direction:
                if 0 <= i + ci < R and 0 <= j + cj < C and visited[i + ci][j + cj] == 0 and (field[i + ci][j + cj] == -field[i][j] or field[i + ci][j + cj] == field[i][j]):
                    stack.append([i + ci, j + cj])
                    visited[i + ci][j + cj] = 1
        else: # 현재 위치가 출구 (-)
            for ci, cj in direction:
                if 0 <= i + ci < R and 0 <= j + cj < C and visited[i + ci][j + cj] == 0 and field[i + ci][j + cj] != 0:
                    stack.append([i + ci, j + cj])
                    visited[i + ci][j + cj] = 1

    # 최종 행 : southest -> 결과에 더하기
    # print('southest : ', southest + 1)
    result += southest + 1
    # 다음 골렘 마킹을 위한 후처리
    golem_num += 1

print(result)