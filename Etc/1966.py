from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    importance = deque(list(map(int, input().split())))

    for i, elem in enumerate(importance):
        importance[i] = (i, elem)
    
    result = 1
    while True:
        if importance[0] == max(importance, key = lambda x:x[1]):
            temp = importance.popleft()
            if temp[0] == m:
                print(result)
                break
            result += 1
        else:
            temp = importance.popleft()
            importance.append(temp)