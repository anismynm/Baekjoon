import sys
input = sys.stdin.readline

M = int(input())
S = []

for _ in range(M):
    commend = list(input().rstrip().split())
    if commend[0] == 'add':
        if int(commend[1]) not in S:
            S.append(int(commend[1]))
    elif commend[0] == 'remove':
        if int(commend[1]) in S:
            S.remove(int(commend[1]))
    elif commend[0] == 'check':
        if int(commend[1]) in S:
            print(1)
        else:
            print(0)
    elif commend[0] == 'toggle':
        if int(commend[1]) in S:
            S.remove(int(commend[1]))
        else:
            S.append(int(commend[1]))
    elif commend[0] == 'all':
        S = list(i for i in range(1, 21))
    elif commend[0] == 'empty':
        S = []
