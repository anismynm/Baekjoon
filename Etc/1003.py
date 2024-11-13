import sys
sys.setrecursionlimit(10000000)
T = int(input())

for _ in range(T):
    n = int(input())
    zeroone = []
    for i in range(n + 1):
        if i == 0:
            zeroone.append([1, 0])
        elif i == 1:
            zeroone.append([0, 1])
        else:
            zeroone.append([zeroone[i - 1][0] + zeroone[i - 2][0], zeroone[i - 1][1] + zeroone[i - 2][1]])
    print(zeroone[-1][0], zeroone[-1][1])