from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
result = []

# BFS
def calc(num, command):
    if command == 'D':
        return (2 * num) % 10000
    elif command == 'S':
        return (num - 1) % 10000
    elif command == 'L':
        return num * 10 % 10000 + num // 1000
    else:
        return num % 10 * 1000 + num // 10

for _ in range(n):
    visited = [0 for _ in range(10000)]
    start, end = map(int, input().split())
    stack = deque([(start, '')])
    visited[start] = 1
    while stack:
        item = stack.popleft()
        if item[0] == end:
            result.append(item[1])
            break
        for command in ('D', 'S', 'L', 'R'):
            num = calc(item[0], command)
            if not visited[num]:
                stack.append((num, item[1] + command))
                visited[num] = 1

for i in result:
    print(i)