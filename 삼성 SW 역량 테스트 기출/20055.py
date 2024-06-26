import sys
input = sys.stdin.readline

N, K = map(int, input().split())
durability = list(map(int, input().split()))

robot = [False for _ in range(N)]
level = 0

while (True):
    level += 1
    
    durability.insert(0, durability.pop(-1))
    robot.insert(0, robot.pop(-1))
    if (robot[N - 1] == True):
        robot[N - 1] = False
    
    for i in range(N - 2, -1, -1):
        if (robot[i] == True):
            if (robot[i + 1] == False and durability[i + 1] > 0):
                robot[i + 1] = True
                robot[i] = False
                durability[i + 1] -= 1
    if (robot[N - 1] == True):
        robot[N - 1] = False

    if (durability[0] > 0):
        robot[0] = True
        durability[0] -= 1

    if (durability.count(0) >= K):
        break

print(level)