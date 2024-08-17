import sys
input = sys.stdin.readline

n, m = map(int, input().split())
is_prime = [True for _ in range(m + 1)]

for i in range(2, int(m ** 0.5) + 1):
    if is_prime[i] == True:          
        for j in range(i+i, m + 1, i): 
            is_prime[j] = False

for i in range(n, m + 1):
    if i == 0 or i == 1:
        continue
    if is_prime[i] == True:
        print(i)