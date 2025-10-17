import sys
input = sys.stdin.readline

N = int(input())
switch = [-1]
switch.extend(list(map(int, input().split())))

sn = int(input())
for _ in range(sn):
    gender, num = map(int, input().split())
    # 남
    if gender == 1:
        for i in range(num, N + 1, num):
            switch[i] = 1 if switch[i] == 0 else 0
    # 여
    else:
        i = 1
        switch[num] = 1 if switch[num] == 0 else 0
        while num - i > 0 and num + i <= N and switch[num - i] == switch[num + i]:
            switch[num - i] = switch[num + i] = 1 if switch[num - i] == 0 else 0
            i += 1
    
for i in range(1, N + 1):
    if i % 20:
        print(switch[i], end = ' ')
    else:
        print(switch[i]) 