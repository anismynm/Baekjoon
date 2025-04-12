## 2025.03.24
## 1H 57M
N, L = map(int, input().split())
field = []
answer = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    set = [0 for _ in range(N)]
    pos = 0
    while pos < N - 1:
        if temp[pos + 1] == temp[pos]:
            pos += 1
        elif temp[pos + 1] == temp[pos] - 1 and pos < N - L:
            able = True
            for i in range(pos + 1, pos + 1 + L):
                set[i] = 1
                if temp[i] != temp[pos] - 1:
                    able = False
                    break
            if not able:
                break
            pos += L
        elif temp[pos + 1] == temp[pos] + 1 and pos >= L - 1:
            able = True
            for i in range(pos - L + 1, pos + 1):
                if set[i] == 1 or temp[i] != temp[pos]:
                    able = False
                    break
            if not able:
                break
            pos += 1
        else:
            break
    if pos >= N - 1:
        answer += 1
    field.append(temp)

field = list(map(list, zip(*field)))

for row in range(N):
    temp = field[row]
    set = [0 for _ in range(N)]
    pos = 0
    while pos < N - 1:
        if temp[pos + 1] == temp[pos]:
            pos += 1
        elif temp[pos + 1] == temp[pos] - 1 and pos < N - L:
            able = True
            for i in range(pos + 1, pos + 1 + L):
                set[i] = 1
                if temp[i] != temp[pos] - 1:
                    able = False
                    break
            if not able:
                break
            pos += L
        elif temp[pos + 1] == temp[pos] + 1 and pos >= L - 1:
            able = True
            for i in range(pos - L + 1, pos + 1):
                if set[i] == 1 or temp[i] != temp[pos]:
                    able = False
                    break
            if not able:
                break
            pos += 1
        else:
            break
    if pos >= N - 1:
        answer += 1

print(answer)