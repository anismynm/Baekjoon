from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

balloon = deque(enumerate(list(map(int, input().split())), start = 1))

while balloon:
    index, rotate = balloon.popleft()
    print(index, end = " ")
    if rotate > 0:
        balloon.rotate(-(rotate - 1))
    else:
        balloon.rotate(-rotate)

print()