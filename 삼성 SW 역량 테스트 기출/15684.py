## 2025.03.25
## 1H 2M 틀
## 1H 20M 시간 초과
## 2H 10M
## DFS는 deepcopy 쓰기 전에 BackTracking으로 생각해보기.

N, M, H = map(int, input().split())
ladder = [[0 for _ in range(N)] for _ in range(H)]
answer = 4

def find(temp):
    for i in range(N):
        pos = i
        h = 0
        while h < H:
            if temp[h][pos] != 0:
                if pos > 0 and temp[h][pos - 1] == temp[h][pos]:
                    pos -= 1
                elif pos < N - 1 and temp[h][pos + 1] == temp[h][pos]:
                    pos += 1
            h += 1
        if pos != i:
            return False
    return True


def dfs(trial, ladder, pp, x):
    global answer
    if answer <= trial:
        return
    if find(ladder) and trial < answer:
        answer = trial
        return

    for i in range(x, N - 1):
        for j in range(H):
            if ladder[j][i] == 0 and ladder[j][i + 1] == 0:
                ladder[j][i] = ladder[j][i + 1] = pp
                dfs(trial + 1, ladder, pp + 1, i)
                ladder[j][i] = ladder[j][i + 1] = 0

pp = 1
for i in range(M):
    a, b = map(int, input().split())
    ladder[a - 1][b - 1] = ladder[a - 1][b] = pp
    pp += 1

dfs(0, ladder, pp, 0)
if answer == 4:
    print(-1)
else:
    print(answer)