import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_list = []
value_list = []

for i in range(N):
    name, value = input().split()
    name_list.append(name)
    value_list.append(int(value))

def lower_bound(num): # num 이상의 값이 처음으로 나오는 곳 찾기
    min = 0
    max = len(value_list) - 1
    result = None
    while min <= max:
        mid = (min + max) // 2
        if num <= value_list[mid]: 
            max = mid - 1
            result = name_list[mid] # num 이상 이면 답이 될 수도 있으니 일단 저장
        else: # num보다 작으면 제외
            min = mid + 1
    return result

for i in range(M):
    print(lower_bound(int(input())))