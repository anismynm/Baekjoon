import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
num_arr = []
sum_arr = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    num_arr.append(list(map(int, input().split())))

sum_arr[0][0] = num_arr[0][0]
for i in range(1, N):
    sum_arr[0][i] = sum_arr[0][i - 1] + num_arr[0][i]
    sum_arr[i][0] = sum_arr[i - 1][0] + num_arr[i][0]

for i in range(1, N):
    for j in range(1, N):
        sum_arr[i][j] = sum_arr[i - 1][j] + sum_arr[i][j - 1] + num_arr[i][j] - sum_arr[i - 1][j - 1]

for i in range(M):
    si, sj, ei, ej = map(int, input().split())
    if si > 1 and sj > 1:
        result.append(sum_arr[ei - 1][ej - 1] - (sum_arr[ei - 1][sj - 2] + sum_arr[si - 2][ej - 1]) + sum_arr[si - 2][sj - 2])
    elif si > 1: # sj = 1
        result.append(sum_arr[ei - 1][ej - 1] - sum_arr[si - 2][ej - 1])
    elif sj > 1: # si = 1
        result.append(sum_arr[ei - 1][ej - 1] - sum_arr[ei - 1][sj - 2])
    else:
        result.append(sum_arr[ei - 1][ej - 1])
    
for num in result:
    print(num)