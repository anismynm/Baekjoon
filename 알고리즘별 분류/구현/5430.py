from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    command = input().rstrip()
    length = int(input())
    lst = deque(eval(input().rstrip()))
    reverse = False
    error = False
    for comm in command:
        if comm == 'R':
            reverse = not reverse
        else:
            if lst:
                if reverse:
                    lst.pop()
                else:
                    lst.popleft()
            else:
                error = True
                break
    if error:
        result.append('error')
    else:
        if reverse:
            result.append(list(reversed(lst)))
        else:
            result.append(list(lst))

for i in result:
    if i == 'error':
        print(i)
    else:
        print('[', end = '')
        for j in range(len(i)):
            if j == len(i) - 1:
                print(i[j], end = '')
            else:
                print('{},'.format(i[j]), end = '')
        print(']')