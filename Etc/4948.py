import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    prime_list = [True] * (2 * n)
    for i in range(1, n):
        if prime_list[i]:
            for j in range(i, 2 * n, i + 1):
                prime_list[j] = False
    print(prime_list[n:2*n].count(True))