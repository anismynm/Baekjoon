N, M = map(int, input().split())

checkboard = []
for _ in range(N):
    checkboard.append(input())

result = 10000
temp = 0
for i in range(N - 7):
    for j in range(M - 7):
        for color in ['B', 'W']:
            temp = 0
            for p in range(i, i + 8):
                for q in range(j, j + 8):
                    if (p + q) % 2 == 0 and checkboard[p][q] != color:
                        temp += 1
                    if (p + q) % 2 != 0 and checkboard[p][q] == color:
                        temp += 1                    
            if temp < result:
                result = temp 

print(result)               