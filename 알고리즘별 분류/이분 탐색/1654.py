import sys
input = sys.stdin.readline

def binary_search(cable, start, end):
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for elem in cable:
            count += elem // mid
        if count >= N:
            temp = mid
            start = mid + 1
        else:
            end = mid - 1
    return temp

K, N = map(int, input().split())
cable = []

for _ in range(K):
    cable.append(int(input()))

print(binary_search(cable, 1, sum(cable) // N))