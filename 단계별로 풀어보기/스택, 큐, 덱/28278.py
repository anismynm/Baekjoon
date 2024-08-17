import sys
stacklist = list()
top = -1

count = int(input())

for i in range(count):
    menu = list(map(int, sys.stdin.readline().split()))

    match (menu[0]):
        case 1:
            stacklist.append(menu[1])
            top += 1

        case 2:
            if (top == -1):
                print(-1)
                continue
            print(stacklist.pop())
            top -= 1

        case 3:
            print(top + 1)

        case 4:
            if (top == -1):
                print(1)
            else:
                print(0)

        case 5:
            if (top == -1):
                print(-1)
                continue
            print(stacklist[-1])
