import sys
input = sys.stdin.readline

people = int(input())
t_size = list(map(int, input().split()))
t, p = map(int, input().split())
result_t = 0

for elem in t_size:
    if elem % t == 0:
        result_t += (elem // t)
    else:
        result_t += (elem // t) + 1

print(result_t)
print('{} {}'.format(people // p, people % p))