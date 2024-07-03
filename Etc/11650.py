import sys
input = sys.stdin.readline

n = int(input())
point = []
for _ in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

point.sort(key = lambda x : x[1])
point.sort(key = lambda x : x[0])

for i in point:
    print('{} {}'.format(i[0], i[1]))