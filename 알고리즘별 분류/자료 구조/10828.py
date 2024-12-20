import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command_list = list(input().rstrip().split())
    if command_list[0] == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif command_list[0] == 'size':
        print(len(stack))
    elif command_list[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif command_list[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(int(command_list[1]))
