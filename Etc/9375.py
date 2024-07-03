from itertools import combinations
import sys
input = sys.stdin.readline

T = int(input())
clothes_dict = {}
result_for_print = []

for _ in range(T):
    clothes_dict.clear()
    result = 0
    n = int(input())

    # 옷 이름, 종류 map 생성
    for _ in range(n):
        name, category = input().rstrip().split()
        if clothes_dict.get(category):
            clothes_dict[category] += 1
        else:
            clothes_dict[category] = 1

    # 조합 따라서 개수 구하기
    result = 1
    name_list = list(clothes_dict.values())
    for elem in name_list:
        result *= (elem + 1)
    result -= 1
    result_for_print.append(result)

for i in result_for_print:
    print(i)