import sys
input = sys.stdin.readline

n = int(input())
count_list = [0] * 10000

for _ in range(n):
    num = int(input())
    count_list[num - 1] += 1

for i, elem in enumerate(count_list):
    for _ in range(elem):
        print(i + 1)