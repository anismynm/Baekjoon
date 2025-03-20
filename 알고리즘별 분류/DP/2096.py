import sys
input = sys.stdin.readline

n = int(input())
max_temp = min_temp = list(map(int, input().split()))

for i in range(1, n):
    field = list(map(int, input().split()))
    max_temp = [max(max_temp[:2]) + field[0], max(max_temp) + field[1], max(max_temp[1:]) + field[2]]
    min_temp = [min(min_temp[:2]) + field[0], min(min_temp) + field[1], min(min_temp[1:]) + field[2]]

print(max(max_temp), min(min_temp))