import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())
num_list = []
result = []
for _ in range(n):
    num_list.append(int(input()))

for iter in permutations(num_list, k):
    temp = int(''.join(str(x) for x in iter))
    if temp not in result:
        result.append(temp)

print(len(result))