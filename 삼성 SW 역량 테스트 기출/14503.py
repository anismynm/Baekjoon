import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

room = []
cleaned_area = 0

for i in range(N):
    room.append(list(map(int, input().split())))

while room[r][c] != 1:
    if room[r][c] == 0:
        room[r][c] = 2
        cleaned_area += 1

    all_cleaned = True
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]
        if ((x < 0) or (x >= N) or (y < 0) or (y >= M)):
            continue
        if (room[x][y] == 0): # 청소 되지 않은 빈 칸 있음
            all_cleaned = False
            break

    if (all_cleaned): # 청소 되지 않은 빈 칸이 없음
        r += dx[(d + 2) % 4]
        c += dy[(d + 2) % 4]
    else: # 청소 되지 않은 빈 칸이 있음
        while (True):
            d = (d + 3) % 4
            x = r + dx[d]
            y = c + dy[d]
            if ((x < 0) or (x >= N) or (y < 0) or (y >= M)):
                continue
            if room[x][y] == 0:
                r = x
                c = y
                break
        
print(cleaned_area)