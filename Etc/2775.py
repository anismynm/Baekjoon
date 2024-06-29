import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a = int(input())
    b = int(input())
    apartment = [i for i in range(1, b + 1)]
    for _ in range(a):
        for i in range(1, b):
            apartment[i] += apartment[i - 1]
    print(apartment[-1])