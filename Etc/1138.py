import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
result = []

for i in range(n - 1, -1, -1):
    if i == n - 1:
        result.append(i + 1)
    else:
        result.insert(line[i], i + 1)

for i in result:
    print(i, end = ' ')
print()