import sys
input = sys.stdin.readline

n = int(input())
prime_list = list(map(int, input().split()))
result = 0

for elem in prime_list:
    if elem == 1:
        continue
    is_prime = True
    for i in range(2, elem):
        if elem % i == 0:
            is_prime = False
            break

    if is_prime:
        result += 1

print(result)