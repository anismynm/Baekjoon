## 2025.03.23
## 1H 11M 0인 CASE 생각하기.
## 2차원 배열 회전

import copy

N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))
result = max([max(i) for i in field])

def sweep(temp): # to_left
    for t, row in enumerate(temp):
        nums = [num for num in row if num != 0]
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        nums = [num for num in nums if num != 0]
        nums += [0] * (N - len(nums))
        temp[t] = nums
    return temp

def dfs(field, trial, dir):
    global result
    if trial == 5:
        num = max([max(i) for i in field])
        if num > result:
            result = num
        return

    temp_field = copy.deepcopy(field)
    if dir == 0: # up
        temp_field = list(map(list, zip(*temp_field)))
        temp_field = sweep(temp_field)
        temp_field = list(map(list, zip(*temp_field)))

    elif dir == 1: # down
        temp_field = list(map(list, zip(*temp_field)))
        temp_field = [x[::-1] for x in temp_field]
        temp_field = sweep(temp_field)
        temp_field = [x[::-1] for x in temp_field]
        temp_field = list(map(list, zip(*temp_field)))

    elif dir == 2: # left
        temp_field = sweep(temp_field)

    else: # 3, right
        temp_field = [x[::-1] for x in temp_field]
        temp_field = sweep(temp_field)
        temp_field = [x[::-1] for x in temp_field]

    if temp_field == field:
        return
    dfs(temp_field, trial + 1, 0)
    dfs(temp_field, trial + 1, 1)
    dfs(temp_field, trial + 1, 2)
    dfs(temp_field, trial + 1, 3)

dfs(field, 0, 0)
dfs(field, 0, 1)
dfs(field, 0, 2)
dfs(field, 0, 3)

print(result)