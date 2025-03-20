arr = [1, 2, 3, 4]
visited = [False] * len(arr)
## (n, new_arr), (n, new_arr, c)
## Permutations만 visited 필요, Combinations는 다음 인덱스로 넘기냐, 안넘기냐로 replacement 차이 발생

## Permutations (순열, 순서 O, 중복 X)
def permutations(n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            permutations(n, new_arr + [arr[i]])
            visited[i] = False

## Product (중복 순열, 순서 O, 중복 O)
def permutation_with_replacement(n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        permutation_with_replacement(n, new_arr + [arr[i]])

## Combinations (조합, 순서 X, 중복 X)
def combinations(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i + 1)

## Combinations_with_replacement (중복 조합, 순서 X, 중복 O)
def combinations_with_replacement(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations_with_replacement(n, new_arr + [arr[i]], i)