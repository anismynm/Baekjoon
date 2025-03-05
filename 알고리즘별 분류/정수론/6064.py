## math.gcd, math.lcm : 최대공약수, 최소공배수
T = int(input())
result = []

for _ in range(T):
    M, N, x, y = map(int, input().split())
    found = False
    i = x
    while i <= M * N:
        if (i - x) % M == 0 and (i - y) % N == 0:
            result.append(i)
            found = True
            break
        else:
            i += M
    if not found:
        result.append(-1)

for num in result:
    print(num)