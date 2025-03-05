from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ladder = []
snake = []
visited = [0 for _ in range(101)]
cnt = -1

for _ in range(N):
    temp = tuple(map(int, input().split()))
    visited[temp[0]] = 2
    ladder.append(temp)

for _ in range(M):
    temp = tuple(map(int, input().split()))
    visited[temp[0]] = -1
    snake.append(temp)

stack = deque([1])
temp_stack = deque([1])
while temp_stack:
    temp_stack.clear()
    while stack:
        cur = stack.popleft()
        if cur == 100:
            temp_stack.clear()
            break
        for i in range(1, 7):
            if 1 <= cur + i <= 100 and visited[cur + i] != 1:
                if visited[cur + i] == 2:
                    n = next(b for a, b in ladder if a == cur + i)
                    visited[n] = 1
                    temp_stack.append(n)
                elif visited[cur + i] == -1:
                    n = next(b for a, b in snake if a == cur + i)
                    visited[n] = 1
                    temp_stack.append(n)
                else:
                    visited[cur + i] = 1
                    temp_stack.append(cur + i)
    stack = copy.deepcopy(temp_stack)
    cnt += 1

print(cnt)