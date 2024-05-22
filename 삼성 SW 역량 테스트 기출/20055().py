from collections import deque
import sys
input = sys.stdin.readline

N, K = int(input().split())
belt = deque(list(map(int, input().split())))
durable = 0
count_level = 1

while (durable < K):
    belt.rotate(1) # 벨트 회전
    


    if belt[0] > 0:
        belt[0] -= 1
        if (belt[0] == 0):
            durable += 1
            if durable < K:
                break