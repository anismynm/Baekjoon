import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
ordered_num = sorted(num_list)
order_dict = {}

i = 0
for elem in ordered_num:
    if not order_dict.get(elem) and order_dict.get(elem) != 0:
        order_dict[elem] = i
        i += 1

for num in num_list:
    print(order_dict.get(num), end = ' ')
print()