from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
stack = []
input_to_make = deque([])
result = []

for _ in range(n):
    input_to_make.append(int(input()))

push_num = 1
while input_to_make:
    if push_num <= input_to_make[0]:
        stack.append(push_num)
        result.append('+')
        push_num += 1
    
    if stack[-1] == input_to_make[0]:
        stack.pop()
        input_to_make.popleft()
        result.append('-')
    elif stack[-1] > input_to_make[0]:
        print('NO')
        break

if not input_to_make:
    for i in result:
        print(i)