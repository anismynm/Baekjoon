## 2025.03.20
## 3H 24M
from collections import deque
N, M = map(int, input().split()) # 세로, 가로
red = (0, 0)
blue = (0, 0)
hole = (0, 0)

def to_left(board, red, blue):
    moved_red = red
    moved_blue = blue
    board[red[0]][red[1]] = 'R'
    board[blue[0]][blue[1]] = 'B'

    if red[0] == blue[0] and blue[1] < red[1]: # CASE : #.B.R..#
        for pos_y in range(blue[1] - 1, -1, -1):
            if board[blue[0]][pos_y] == '.':
                board[blue[0]][pos_y] = 'B'
                board[blue[0]][pos_y + 1] = '.'
            elif board[blue[0]][pos_y] == 'O':
                return False
            elif board[blue[0]][pos_y] == '#':
                moved_blue = (blue[0], pos_y + 1)
                break
            else:
                print("ERROR 1")
                exit()
        for pos_y in range(red[1] - 1, -1, -1):
            if board[red[0]][pos_y] == '.':
                board[red[0]][pos_y] = 'R'
                board[red[0]][pos_y + 1] = '.'
            elif board[red[0]][pos_y] == 'O': # CASE : #B..#OR.#
                return True
            else: # CASE : (#BR...#), (#B.#R.#)
                moved_red = (red[0], pos_y + 1)
                break

    elif red[0] == blue[0] and red[1] < blue[1]: # CASE : #.R...B#
        for pos_y in range(red[1] - 1, -1, -1):
            if board[red[0]][pos_y] == '.':
                board[red[0]][pos_y] = 'R'
                board[red[0]][pos_y + 1] = '.'
            elif board[red[0]][pos_y] == 'O':
                board[red[0]][pos_y + 1] = '.'
                for pos_yy in range(blue[1] - 1, pos_y, -1):
                    if board[red[0]][pos_yy] == '#':
                        return True
                return False
            elif board[red[0]][pos_y] == '#':
                moved_red = (red[0], pos_y + 1)
                break
            else:
                print("ERROR 2")
                exit()
        for pos_y in range(blue[1] - 1, -1, -1):
            if board[blue[0]][pos_y] == '.':
                board[blue[0]][pos_y] = 'B'
                board[blue[0]][pos_y + 1] = '.'
            elif board[blue[0]][pos_y] == 'O':
                return False
            else:
                moved_blue = (blue[0], pos_y + 1)
                break

    else: # red, blue의 pos_x가 다름.
        for pos_y in range(red[1] - 1, -1, -1):
            if board[red[0]][pos_y] == '.':
                board[red[0]][pos_y] = 'R'
                board[red[0]][pos_y + 1] = '.'
            elif board[red[0]][pos_y] == 'O':
                return True
            elif board[red[0]][pos_y] == '#':
                moved_red = (red[0], pos_y + 1)
                break
            else:
                print("ERROR 3")
                exit()
        for pos_y in range(blue[1] - 1, -1, -1):
            if board[blue[0]][pos_y] == '.':
                board[blue[0]][pos_y] = 'B'
                board[blue[0]][pos_y + 1] = '.'
            elif board[blue[0]][pos_y] == 'O':
                return False
            elif board[blue[0]][pos_y] == '#':
                moved_blue = (blue[0], pos_y + 1)
                break
            else:
                print("ERROR 4")
                exit()
    return [moved_red, moved_blue]

def to_right(board, red, blue):
    moved_red = red
    moved_blue = blue
    board[red[0]][red[1]] = 'R'
    board[blue[0]][blue[1]] = 'B'

    if red[0] == blue[0] and red[1] < blue[1]: # CASE : #.R...B.#
        for pos_y in range(blue[1] + 1, M):
            if board[blue[0]][pos_y] == '.':
                board[blue[0]][pos_y] = 'B'
                board[blue[0]][pos_y - 1] = '.'
            elif board[blue[0]][pos_y] == '#':
                moved_blue = (blue[0], pos_y - 1)
                break
            elif board[blue[0]][pos_y] == 'O':
                return False
            else:
                print("ERROR 5", board[blue[0]][pos_y])
                exit()
        for pos_y in range(red[1] + 1, M):
            if board[red[0]][pos_y] == '.':
                board[red[0]][pos_y] = 'R'
                board[red[0]][pos_y - 1] = '.'
            elif board[red[0]][pos_y] == '#':
                moved_red = (red[0], pos_y - 1)
                break
            elif board[red[0]][pos_y] == 'O':
                return True
            else:
                moved_red = (red[0], pos_y - 1)
                break

    elif red[0] == blue[0] and blue[1] < red[1]: # CASE : #..B..R...#
        for pos_y in range(red[1] + 1, M):
            if board[red[0]][pos_y] == '.':
                board[red[0]][pos_y] = 'R'
                board[red[0]][pos_y - 1] = '.'
            elif board[red[0]][pos_y] == 'O': # CASE : #..B..RO..#
                board[red[0]][pos_y - 1] = '.'
                for pos_yy in range(blue[1] + 1, pos_y):
                    if board[blue[0]][pos_yy] == '#':
                        return True
                return False
            elif board[red[0]][pos_y] == '#':
                moved_red = (red[0], pos_y - 1)
                break
            else:
                print("ERROR 6")
                exit()
        for pos_y in range(blue[1] + 1, M):
            if board[blue[0]][pos_y] == '.':
                board[blue[0]][pos_y] = 'B'
                board[blue[0]][pos_y - 1] = '.'
            elif board[blue[0]][pos_y] == 'O':
                return False
            else:
                moved_blue = (blue[0], pos_y - 1)
                break

    else:
        for pos_y in range(red[1] + 1, M):
            if board[red[0]][pos_y] == '.':
                board[red[0]][pos_y] = 'R'
                board[red[0]][pos_y - 1] = '.'
            elif board[red[0]][pos_y] == 'O':
                return True
            elif board[red[0]][pos_y] == '#':
                moved_red = (red[0], pos_y - 1)
                break
            else:
                print("ERROR 7")
                exit()
        for pos_y in range(blue[1] + 1, M):
            if board[blue[0]][pos_y] == '.':
                board[blue[0]][pos_y] = 'B'
                board[blue[0]][pos_y - 1] = '.'
            elif board[blue[0]][pos_y] == 'O':
                return False
            elif board[blue[0]][pos_y] == '#':
                moved_blue = (blue[0], pos_y - 1)
                break
            else:
                print("ERROR 8")
                exit()
    return [moved_red, moved_blue]

def to_upper(board, red, blue):
    moved_red = red
    moved_blue = blue
    board[red[0]][red[1]] = 'R'
    board[blue[0]][blue[1]] = 'B'

    if red[1] == blue[1] and blue[0] < red[0]:  # CASE : BLUE가 RED 바로 위
        for pos_x in range(blue[0] - 1, -1, -1):
            if board[pos_x][blue[1]] == '.':
                board[pos_x][blue[1]] = 'B'
                board[pos_x + 1][blue[1]] = '.'
            elif board[pos_x][blue[1]] == 'O':
                return False
            elif board[pos_x][blue[1]] == '#':
                moved_blue = (pos_x + 1, blue[1])
                break
            else:
                print("ERROR 9")
                exit()
        for pos_x in range(red[0] - 1, -1, -1):
            if board[pos_x][red[1]] == '.':
                board[pos_x][red[1]] = 'B'
                board[pos_x + 1][red[1]] = '.'
            elif board[pos_x][red[1]] == 'O':  # CASE : #B..#OR.#
                return True
            else:  # CASE : (#BR...#), (#B.#R.#)
                moved_red = (pos_x + 1, red[1])
                break

    elif red[1] == blue[1] and red[0] < blue[0]:  # CASE : RED가 BLUE 바로 위
        for pos_x in range(red[0] - 1, -1, -1):
            if board[pos_x][red[1]] == '.':
                board[pos_x][red[1]] = 'R'
                board[pos_x + 1][red[1]] = '.'
            elif board[pos_x][red[1]] == 'O':
                board[pos_x + 1][red[1]] = '.'
                for pos_xx in range(blue[0] - 1, pos_x, -1):
                    if board[pos_xx][blue[1]] == '#':
                        return True
                return False
            elif board[pos_x][red[1]] == '#':
                moved_red = (pos_x + 1, red[1])
                break
            else:
                print("ERROR 10")
                exit()
        for pos_x in range(blue[0] - 1, -1, -1):
            if board[pos_x][blue[1]] == '.':
                board[pos_x][blue[1]] = 'B'
                board[pos_x + 1][blue[1]] = '.'
            elif board[pos_x][blue[1]] == 'O':
                return False
            else:
                moved_blue = (pos_x + 1, blue[1])
                break

    else:  # red, blue의 pos_x가 다름.
        for pos_x in range(red[0] - 1, -1, -1):
            if board[pos_x][red[1]] == '.':
                board[pos_x][red[1]] = 'R'
                board[pos_x + 1][red[1]] = '.'
            elif board[pos_x][red[1]] == 'O':
                return True
            elif board[pos_x][red[1]] == '#':
                moved_red = (pos_x + 1, red[1])
                break
            else:
                print("ERROR 11, ",board[pos_x][red[1]])
                exit()
        for pos_x in range(blue[0] - 1, -1, -1):
            if board[pos_x][blue[1]] == '.':
                board[pos_x][blue[1]] = 'B'
                board[pos_x + 1][blue[1]] = '.'
            elif board[pos_x][blue[1]] == 'O':
                return False
            elif board[pos_x][blue[1]] == '#':
                moved_blue = (pos_x + 1, blue[1])
                break
            else:
                print("ERROR 12")
                exit()
    return [moved_red, moved_blue]

def to_lower(board, red, blue):
    moved_red = red
    moved_blue = blue
    board[red[0]][red[1]] = 'R'
    board[blue[0]][blue[1]] = 'B'

    if red[1] == blue[1] and red[0] < blue[0]: # CASE : BLUE가 RED 바로 아래
        for pos_x in range(blue[0] + 1, N):
            if board[pos_x][blue[1]] == '.':
                board[pos_x][blue[1]] = 'B'
                board[pos_x - 1][blue[1]] = '.'
            elif board[pos_x][blue[1]] == '#':
                moved_blue = (pos_x - 1, blue[1])
                break
            elif board[pos_x][blue[1]] == 'O':
                return False
            else:
                print("ERROR 13")
                exit()
        for pos_x in range(red[0] + 1, N):
            if board[pos_x][red[1]] == '.':
                board[pos_x][red[1]] = 'R'
                board[pos_x - 1][red[1]] = '.'
            elif board[pos_x][red[1]] == '#':
                moved_red = (pos_x - 1, red[1])
                break
            elif board[pos_x][red[1]] == 'O':
                return True
            else:
                moved_red = (pos_x - 1, red[1])
                break

    elif red[1] == blue[1] and blue[0] < red[0]: # CASE : RED가 BLUE 바로 아래
        for pos_x in range(red[0] + 1, N):
            if board[pos_x][red[1]] == '.':
                board[pos_x][red[1]] = 'R'
                board[pos_x - 1][red[1]] = '.'
            elif board[pos_x][red[1]] == 'O': # CASE : #..B..RO..#
                board[pos_x - 1][red[1]] = '.'
                for pos_xx in range(blue[1] + 1, pos_x):
                    if board[pos_xx][blue[1]] == '#':
                        return True
                return False
            elif board[pos_x][red[1]] == '#':
                moved_red = (pos_x - 1, red[1])
                break
            else:
                print("ERROR 14")
                exit()
        for pos_x in range(blue[0] + 1, N):
            if board[pos_x][blue[1]] == '.':
                board[pos_x][blue[1]] = 'B'
                board[pos_x - 1][blue[1]] = '.'
            elif board[pos_x][blue[1]] == 'O':
                return False
            else:
                moved_blue = (pos_x - 1, blue[1])
                break

    else:
        for pos_x in range(red[0] + 1, N):
            if board[pos_x][red[1]] == '.':
                board[pos_x][red[1]] = 'R'
                board[pos_x - 1][red[1]] = '.'
            elif board[pos_x][red[1]] == 'O':
                return True
            elif board[pos_x][red[1]] == '#':
                moved_red = (pos_x - 1, red[1])
                break
            else:
                print("ERROR 15")
                exit()
        for pos_x in range(blue[0] + 1, N):
            if board[pos_x][blue[1]] == '.':
                board[pos_x][blue[1]] = 'B'
                board[pos_x - 1][blue[1]] = '.'
            elif board[pos_x][blue[1]] == 'O':
                return False
            elif board[pos_x][blue[1]] == '#':
                moved_blue = (pos_x - 1, blue[1])
                break
            else:
                print("ERROR 16")
                exit()
    return [moved_red, moved_blue]

empty_board = []
for i in range(N):
    temp = list(input())
    if 'R' in temp:
        red = (i, temp.index('R'))
        temp[temp.index('R')] = '.'
    if 'B' in temp:
        blue = (i, temp.index('B'))
        temp[temp.index('B')] = '.'
    if 'O' in temp:
        hole = (i, temp.index('O'))
    empty_board.append(temp)

stack = deque([[red, blue, 0]])
finished_stack = []
while stack:
    red, blue, trial = stack.popleft()
    if trial == 10:
        break
    finished_stack.append([red, blue])

    bfs = []
    bfs.append(to_left([t[:] for t in empty_board], red, blue))
    bfs.append(to_right([t[:] for t in empty_board], red, blue))
    bfs.append(to_upper([t[:] for t in empty_board], red, blue))
    bfs.append(to_lower([t[:] for t in empty_board], red, blue))
    for item in bfs:
        if item == True:
            print(trial + 1)
            exit()
        elif item == False:
            continue
        elif item[0] == red and item[1] == blue:
            continue
        else:
            if item not in finished_stack:
                stack.append([item[0], item[1], trial + 1])
print(-1)