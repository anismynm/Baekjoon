import sys
input = sys.stdin.readline

n = int(input())
str_list = []

for _ in range(n):
    siu = input().rstrip()
    if siu not in str_list:
        str_list.append(siu)

str_list.sort()
str_list.sort(key = lambda x : len(x))

for i in str_list:
    print(i)