import sys
input = sys.stdin.readline

n = int(input())
count_dict = {}
num_card = list(map(int, input().split()))

for elem in num_card:
    if count_dict.get(elem):
        count_dict[elem] += 1
    else:
        count_dict[elem] = 1

m = int(input())
num_card_to_find = list(map(int, input().split()))

for elem in num_card_to_find:
    if count_dict.get(elem):
        print(count_dict.get(elem), end = ' ')
    else:
        print(0, end = ' ')
print()