import sys
input = sys.stdin.readline

n = int(input())
level = []

for _ in range(n):
    level.append(int(input()))

level.sort()
death = 0.15 * n
if death - int(death) < 0.5:
    death = int(death)
else:
    death = int(death) + 1
new_level = level[death:n - death]

if len(new_level):
    result = sum(new_level) / len(new_level)
else:
    print(0)
    exit()

if result - int(result) < 0.5:
    print(int(result))
else:
    print(int(result) + 1)