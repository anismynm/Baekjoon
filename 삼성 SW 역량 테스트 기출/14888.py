## 2025.03.20
## 15M
N = int(input())
num = list(map(int, input().split()))
plus, minus, mult, div = list(map(int, input().split()))
max = -int(1e10)
min = int(1e10)

def dfs(pivot, result, plus, minus, mult, div):
    global max, min
    if pivot == N - 1:
        if result > max:
            max = result
        if result < min:
            min = result
        return
    if plus > 0:
        dfs(pivot + 1, result + num[pivot + 1], plus - 1, minus, mult, div)
    if minus > 0:
        dfs(pivot + 1, result - num[pivot + 1], plus, minus - 1, mult, div)
    if mult > 0:
        dfs(pivot + 1, result * num[pivot + 1], plus, minus, mult - 1, div)
    if div > 0:
        if result > 0:
            dfs(pivot + 1, result // num[pivot + 1], plus, minus, mult, div - 1)
        else:
            dfs(pivot + 1, -(-result // num[pivot + 1]), plus, minus, mult, div - 1)

dfs(0, num[0], plus, minus, mult, div)
print(max)
print(min)