import sys
input = sys.stdin.readline

def bingo_cnt(bingo):
    result = 0
    for row in bingo:
        if sum(row) == 0:
            result += 1
    for i in range(5):
        if sum([bingo[j][i] for j in range(5)]) == 0:
            result += 1
    if sum([bingo[i][i] for i in range(5)]) == 0:
        result += 1
    if sum([bingo[i][4 - i] for i in range(5)]) == 0:
        result += 1
    return result

bingo = []
result = 0

for _ in range(5):
    bingo.append(list(map(int, input().split())))

for _ in range(5):
    nums = list(map(int, input().split()))
    for num in nums:
        result += 1
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == num:
                    bingo[i][j] = 0
                    if bingo_cnt(bingo) >= 3:
                        print(result)
                        exit()