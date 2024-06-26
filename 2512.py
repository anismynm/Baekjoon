import sys
input = sys.stdin.readline

N = int(input())
nation = list(map(int, input().split()))
M = int(input())

result = 0
while sum(nation) != 0:
    flag = True
    max_bugget = M // (len(nation) - nation.count(0))
    for i in range(len(nation)):
        if nation[i] <= max_bugget and nation[i] != 0:
            M -= nation[i]
            if (result < nation[i]):
                result = nation[i]
            nation[i] = 0
            flag = False
    if flag:
        result = max_bugget
        break
    
print(result)