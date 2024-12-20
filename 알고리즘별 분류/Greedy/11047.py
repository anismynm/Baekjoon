from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = deque([])
result = 0

for i in range(N):
    coin.appendleft(int(input()))

for elem in coin:
    result += K // elem
    K = K % elem
    if K == 0:
        print(result)
        break