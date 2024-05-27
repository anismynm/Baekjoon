N = int(input())
seat = [[0] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 오, 왼, 아래, 위
std_dict = {}

def find_index(value, arr):
    for x in range(N):
        for y in range(N):
            if (arr[x][y] == value):
                return x, y

for _ in range(N**2):
    std = list(map(int, input().split()))
    std_dict[std[0]] = [std[1], std[2], std[3], std[4]]

for i, std in enumerate(std_dict.items()):
    if (i == 0):
        seat[1][1] = std[0]           
        # print("처음 {} -> seat({}, {})".format(std[0], 1, 1))
        continue
    elif (i == N**2 - 1):
        for x in range(N):
            for y in range(N):
                if (seat[x][y] == 0):
                    seat[x][y] = std[0]
                    # print("마지막 {} -> seat({}, {})".format(std[0], x, y))
                    break
        continue

    fav_lv = [[0] * N for _ in range(N)]

    # 이미 자리에 사람이 있으면 못 감 (-1)
    for x in range(N):
            for y in range(N):
                if (seat[x][y] != 0):
                    fav_lv[x][y] = -1
    
    # 각 자리의 선호도 계산
    for fav in std[1]:
        fav_seat_x, fav_seat_y = None, None
        for x in range(N):
            for y in range(N):
                if (seat[x][y] == fav):
                    fav_seat_x, fav_seat_y = x, y
        if (fav_seat_x == None and fav_seat_y == None): # 선호하는 사람이 아직 자리에 없으면
            continue            
        for i in range(4):
            nx = fav_seat_x + dx[i]
            ny = fav_seat_y + dy[i]
            if (nx < 0 or nx >= N or ny < 0 or ny >= N):
                continue
            if fav_lv[nx][ny] != -1:
                fav_lv[nx][ny] += 1
    
    # 선호도가 가장 높은 자리가 1개면 끝, 여러 개면 empty로
    max_fav = 0
    max_fav_seat = []
    for x in range(N):
        for y in range(N):
            if (fav_lv[x][y] > max_fav):
                max_fav = fav_lv[x][y]
                max_fav_seat = [(x, y)]
            elif (fav_lv[x][y] == max_fav):
                max_fav_seat.append((x, y))            
    if (len(max_fav_seat) == 1):
        seat[max_fav_seat[0][0]][max_fav_seat[0][1]] = std[0]
        # print("1번 조건 {} -> seat({}, {})".format(std[0], max_fav_seat[0][0], max_fav_seat[0][1]))
        continue
    else:
        for x in range(N):
            for y in range(N):
                if (fav_lv[x][y] != max_fav):
                    fav_lv[x][y] = -1 # 여기까지 하면 선호도 가장 높은 자리 여러개만 값을 가짐
        for x in range(N):
            for y in range(N):
                if (fav_lv[x][y] == max_fav):
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if (nx < 0 or nx >= N or ny < 0 or ny >= N):
                            continue
                        if (seat[nx][ny] == 0): # 옆 자리 비어있으면 선호도 +1 (상하좌우 반복)
                            fav_lv[x][y] += 1
        max_fav = 0
        max_fav_seat = []                    
        for x in range(N):
            for y in range(N):
                if (fav_lv[x][y] > max_fav):
                    max_fav = fav_lv[x][y]
                    max_fav_seat = [(x, y)]
                elif (fav_lv[x][y] == max_fav):
                    max_fav_seat.append((x, y))            
        if (len(max_fav_seat) == 1):
            seat[max_fav_seat[0][0]][max_fav_seat[0][1]] = std[0]
            # print("2번 조건 {} -> seat({}, {})".format(std[0], max_fav_seat[0][0], max_fav_seat[0][1]))
            continue
        else:
            for x in range(N):
                for y in range(N):
                    if (fav_lv[x][y] != max_fav):
                        fav_lv[x][y] = -1 # 여기까지 하면 선호도 같은데다가 인접 빈칸도 같은 여러개만 값을 가짐
            # 이제 최소 행, 없다면 최소 열 찾기
            row_index = []
            for x in range(N):
                for y in range(N):
                    if (fav_lv[x][y] != -1):
                        row_index.append([x, y])
                if len(row_index) == 0:
                    continue
                seat[row_index[0][0]][row_index[0][1]] = std[0]
                # print("3번 조건 {} -> seat({}, {})".format(std[0], row_index[0][0], row_index[0][1]))
                break

# for x in range(N):
#     for y in range(N):
#         print(seat[x][y], end=' ')
#     print()

score = [0, 1, 10, 100, 1000]
result = 0

for x in range(N):
    for y in range(N):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or nx >= N or ny < 0 or ny >= N):
                continue
            if (seat[nx][ny] in std_dict[seat[x][y]]):
                cnt += 1
        result += score[cnt]

print(result)