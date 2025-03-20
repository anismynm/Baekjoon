## 2025.03.20
## 38M
N, M, i, j, K = map(int, input().split())
field = []

def to_east(dice):
    dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    return dice

def to_west(dice):
    dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    return dice

def to_south(dice):
    dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    return dice

def to_north(dice):
    dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    return dice

for _ in range(N):
    field.append(list(map(int, input().split())))
command = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
pos = [i, j]

for com in command:
    if com == 1:
        if pos[1] + 1 == M:
            continue
        pos[1] += 1
        dice = to_east(dice)
    elif com == 2:
        if pos[1] - 1 == -1:
            continue
        pos[1] -= 1
        dice = to_west(dice)
    elif com == 3:
        if pos[0] - 1 == -1:
            continue
        pos[0] -= 1
        dice = to_north(dice)
    else: # 4
        if pos[0] + 1 == N:
            continue
        pos[0] += 1
        dice = to_south(dice)
    if field[pos[0]][pos[1]] == 0:
        field[pos[0]][pos[1]] = dice[5]
    else:
        dice[5] = field[pos[0]][pos[1]]
        field[pos[0]][pos[1]] = 0
    print(dice[0])