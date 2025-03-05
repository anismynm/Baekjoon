import heapq
import sys
input = sys.stdin.readline

N = int(input())
minH = []
result = []
heapq.heapify(minH)

for _ in range(N):
    num = int(input())
    if num == 0:
        if minH:
            temp = heapq.heappop(minH)
            result.append(temp[0] if temp[1] == 1 else -temp[0])
        else:
            result.append(0)
    elif num > 0:
        heapq.heappush(minH, (num, 1))
    else: # num < 0
        heapq.heappush(minH, (-num, 0))

for i in result:
    print(i)