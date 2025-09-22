## union find
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
init = list(map(int, input().split()))
party = []

init.pop(0)
init = set(init)

for _ in range(M):
    tmp = list(map(int, input().split()))
    tmp.pop(0)
    tmp = set(tmp)
    party.append(tmp)
    if tmp & init:
        init.update(tmp)

if not init:
    print(M)
    exit()
else:
    result = 0
    for tmp in party:
        if not tmp & init:
            result += 1
    print(result)