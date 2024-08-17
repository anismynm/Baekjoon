# Pypy3
import sys
input = sys.stdin.readline

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def transfer(coord, speed, direction):
    i, j = coord
    return ((i + speed * di[direction]) % N, (j + speed * dj[direction]) % N)

N, M, K = map(int, input().split())
fireball = []
result = 0

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([(r - 1, c - 1), m, s, d])

for _ in range(K):
    for ball in fireball:
        ball[0] = transfer(ball[0], ball[2], ball[3])
    temp_ball = []
    while fireball:
        coord, m, s, d = fireball.pop()
        count = 1
        same = True
        for i in range(len(fireball)):
            if fireball[i][0] == coord:
                m += fireball[i][1]
                s += fireball[i][2]
                count += 1
                if d % 2 != fireball[i][3] % 2:
                    same = False
        if count != 1:
            fireball = [i for i in fireball if i[0] != coord]
            if m >= 5:
                if same:
                    for i in range(0, 7, 2):
                        temp_ball.append([coord, m // 5, s // count, i])
                else:
                    for i in range(1, 8, 2):
                        temp_ball.append([coord, m // 5, s // count, i])
        else:
            temp_ball.append([coord, m, s, d])
    fireball = temp_ball

for ball in fireball:
    result += ball[1]

print(result)