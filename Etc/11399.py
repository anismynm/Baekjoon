n = int(input())
atm = sorted(list(map(int, input().split())))
print(sum(sum(atm[:i]) for i in range(1, n + 1)))