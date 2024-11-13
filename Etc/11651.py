import sys
input = sys.stdin.readline

N = int(input())
coord = []

for _ in range(N):
    coord.append(list(map(int, input().split())))

coord.sort(key = lambda x:x[0])
coord.sort(key = lambda x:x[1])

for elem in coord:
    print(elem[0], elem[1])