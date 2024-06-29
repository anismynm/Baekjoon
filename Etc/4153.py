import sys
input = sys.stdin.readline

while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break

    max_num = max(x, y, z)

    if (max_num**2 == x**2 + y**2 + z**2 - max_num**2):
        print('right')
    else:
        print('wrong')