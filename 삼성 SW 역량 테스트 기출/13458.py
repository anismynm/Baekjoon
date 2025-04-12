import math
n = int(input())
customer = list(map(int, input().split()))
a_max, b_max = map(int, input().split())

result = n
for num in customer:
    result += math.ceil((num - a_max) / b_max) if num > a_max else 0
print(result)