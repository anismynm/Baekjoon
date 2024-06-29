import sys
input = sys.stdin.readline

def is_prime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

T = int(input())

for _ in range(T):
    n = int(input())
    for i in range(n//2, n):
        if is_prime(i) and is_prime(n - i):
            print('{} {}'.format(n - i, i))
            break