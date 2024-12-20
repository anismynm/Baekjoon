import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
tree = sorted(list(map(int, input().split())), reverse = True)
result = 0

for i in range(n - 1):
    gap = tree[i] - tree[i + 1]
    if result + gap * (i + 1) == m:
        print(tree[i + 1])
        exit()
    elif result + gap * (i + 1) < m:
        result += gap * (i + 1)
    else:
        print(tree[i] - math.ceil((m - result) / (i + 1)))
        exit()

print(tree[-1] - math.ceil((m - result) / n))