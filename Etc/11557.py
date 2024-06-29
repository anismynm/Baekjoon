import sys
input = sys.stdin.readline

max = 0
max_univ = "none"

T = int(input())

for i in range(T):
    N = int(input())

    for j in range(N):
        name, count = input().split()
        if (int(count) > max):
            max = int(count)
            max_univ = name
    print(max_univ)