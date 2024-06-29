from itertools import combinations
import sys
input = sys.stdin.readline

result = []
while True:
    S = list(map(int, input().split()))
    if S[0] == 0:
        break
    test_case = list(combinations(S[1:], 6))
    result.append(test_case)

for elem in result:
    for i in elem:
        print(' '.join(map(str, i)))
    print()