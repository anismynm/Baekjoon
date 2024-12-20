import sys
input = sys.stdin.readline

n = int(input())
register = []

for _ in range(n):
    age, name = input().rstrip().split()
    register.append((int(age), name))

register.sort(key = lambda x : x[0])

for elem in register:
    print('{} {}'.format(elem[0], elem[1]))