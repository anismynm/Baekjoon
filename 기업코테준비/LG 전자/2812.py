N, K = map(int, input().split())
nums = list(int(d) for d in input())
result = []

for num in nums:
    while result and K > 0 and result[-1] < num:
        result.pop()
        K -= 1
    result.append(num)

while K > 0:
    result.pop()
    K -= 1

print(''.join(map(str, result)))