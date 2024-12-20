import sys
input = sys.stdin.readline

def mode(arr):
    count = [0 for _ in range(8001)]
    for elem in arr:
        count[elem + 4000] += 1

    if count.count(max(count)) == 1:
        print(count.index(max(count)) - 4000)
    else:
        count[count.index(max(count))] = 0
        print(count.index(max(count)) - 4000)

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num.sort()
avg = round(sum(num) / n)
mid = num[n // 2]
rng = num[-1] - num[0]

print(avg)
print(mid)
mode(num)
print(rng)