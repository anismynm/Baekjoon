import copy
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
order_dict = {key: i for i, key in enumerate(sorted(list(set(copy.deepcopy(nums)))))}

for num in nums:
    print(order_dict[num], end = ' ')
print()