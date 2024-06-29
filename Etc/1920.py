import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

M = int(input())
input_list = list(map(int, input().split()))

for num in input_list:
    min = 0
    max = len(num_list) - 1
    while min <= max:
        mid = (min + max) // 2
        if num == num_list[mid]:
            print('1')
            break
        elif num < num_list[mid]:
            max = mid - 1
        else:
            min = mid + 1
    if min > max:
        print('0')