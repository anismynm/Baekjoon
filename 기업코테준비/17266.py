import math
# 굴다리의 길이
N = int(input())
# 가로등의 개수
M = int(input())
# 가로등의 위치
location = list(map(int, input().split()))
result = max(location[0], N - location[-1])

interval = []
for i in range(M - 1):
    interval.append((location[i+1] - location[i]) / 2)

if interval:
    result = max(result, math.ceil(max(interval)))

print(result)