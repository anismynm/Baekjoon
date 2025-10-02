import sys
from collections import deque
input = sys.stdin.readline

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = map(int, input().split())
board = []

for _ in range(r):
    board.append(input().rstrip())

result = 0

def dfs(i, j, history, dist):
    global result
    flag = False
    for ni, nj in direction:
        if 0 <= i + ni < r and 0 <= j + nj < c and history[ord(board[i + ni][j + nj]) - 65] == 0:
            flag = True
            history[ord(board[i + ni][j + nj]) - 65] = 1
            dfs(i + ni, j + nj, history, dist + 1)
            history[ord(board[i + ni][j + nj]) - 65] = 0
    if not flag and result < dist:
        result = dist

temp = [0] * 26
temp[ord(board[0][0]) - 65] = 1
dfs(0, 0, temp, 1)
print(result)