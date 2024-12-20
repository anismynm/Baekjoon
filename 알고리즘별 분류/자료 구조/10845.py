from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n):
    command_list = list(input().rstrip().split())
    if command_list[0] == 'pop':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif command_list[0] == 'size':
        print(len(queue))
    elif command_list[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif command_list[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif command_list[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
    else:
        queue.append(int(command_list[1]))