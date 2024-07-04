from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
index = [i for i in range(n)]
friend = [] # 입력받은 배열 (수정 x)
friend_included = [] # 나중에 결과 계산 할 때 쓰일 배열
result = []

for _ in range(n):
    temp = input().rstrip()
    friend.append(temp)
    friend_included.append(list(temp))

# 2-친구 구하기
for elem in combinations(index, 2):
    x = elem[0]
    y = elem[1]
    for i in range(n):
        if friend[i][x] == 'Y' and friend[i][y] == 'Y':
            friend_included[x][y] = 'Y'
            friend_included[y][x] = 'Y'

for i in range(n):
    result.append(friend_included[i].count('Y'))
    
print(max(result))