from collections import deque

N = int(input())
nums = deque(sorted(list(map(int, input().split()))))
i = result = 0

while i < N:
    i += nums[i]
    result += 1

print(result)