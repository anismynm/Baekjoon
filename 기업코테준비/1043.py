## union find
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [n for n in range(N + 1)]

def getParents(a):
    if parents[a] == a:
        return a
    return getParents(parents[a])

def unionParents(a, b):
    a = getParents(a)
    b = getParents(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

know_truth = list(map(int, input().split()))
know_truth.pop(0)
if len(know_truth):
    know_truth.sort()
    for i in know_truth:
        parents[i] = know_truth[0]
    know_truth = know_truth[0]

partys = []

for _ in range(M):
    tmp = list(map(int, input().split()))
    tmp.pop(0)
    tmp.sort()
    partys.append(tmp)
    for a in range(1, len(tmp)):
        unionParents(tmp[0], tmp[a])

if not know_truth:
    print(len(partys))
    exit()

result = 0
while partys:
    party = partys.pop()
    if getParents(know_truth) not in [getParents(i) for i in party]:
        result += 1
print(result)