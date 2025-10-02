from collections import deque
stack = deque(list(input()))
boom = input()

size = len(stack)
boom_size = len(boom)
pivot = 0
while pivot + boom_size <= size:
    if stack[pivot:pivot+boom_size] == boom:
        