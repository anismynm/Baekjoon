import sys
input = sys.stdin.readline

N, L = map(int, input().split())

fruit_list = list(map(int, input().split()))
fruit_list.sort()

for i in fruit_list:
    if (i <= L):
        L += 1

print(L)