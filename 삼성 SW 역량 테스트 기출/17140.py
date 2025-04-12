## 2025.03.23
## 2H 50M
r, c, k = map(int, input().split())
time = 0
field = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    field[i][0], field[i][1], field[i][2] = map(int, input().split())

def sort(row_arr):
    temp = []
    for i in range(1, max(row_arr) + 1):
        cnt = row_arr.count(i)
        if cnt > 0:
            temp.append((i, cnt))
    temp = sorted(temp, key = lambda x:(x[1], x[0]))
    return [item for tup in temp for item in tup]

row = column = 3
while time <= 100:
    if field[r - 1][c - 1] == k:
        print(time)
        exit()
    if row >= column:
        for i in range(row):
            field[i] = sort(field[i])
            if len(field[i]) > 100:
                field[i] = field[i][:100]
                column = 100
            else:
                if i == 0:
                    column = len(field[i])
                if len(field[i]) > column:
                    column = len(field[i])
                field[i].extend([0] * (100 - len(field[i])))
    else:
        field = list(map(list, zip(*field)))
        for i in range(column):
            field[i] = sort(field[i])
            if len(field[i]) > 100:
                field[i] = field[i][:100]
                row = 100
            else:
                if i == 0:
                    row = len(field[i])
                if len(field[i]) > row:
                    row = len(field[i])
                field[i].extend([0] * (100 - len(field[i])))
        field = list(map(list, zip(*field)))
    time += 1

print(-1)