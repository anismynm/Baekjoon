import sys
input = sys.stdin.readline

x_arr = [i for i in input().rstrip()]
y_arr = [i for i in input().rstrip()]
lcs = [[0 for _ in range(len(y_arr))] for _ in range(len(x_arr))]

for i, x in enumerate(x_arr):
    for j, y in enumerate(y_arr):
        if x == y:
            lcs[i][j] = lcs[i - 1][j - 1] + 1 if i != 0 and j != 0 else 1
        else:
            lcs[i][j] = max(lcs[i - 1][j] if i != 0 else 0, lcs[i][j - 1] if j != 0 else 0)

print(max(max([row for row in lcs])))