N, r, c = map(int, input().split())

def dfs(i, j, r, c, n):
    global result
    dir = [(i, j), (i, j + 2 ** (n - 1)), (i + 2 ** (n - 1), j), (i + 2 ** (n - 1), j + 2 ** (n - 1))]
    if n == 1:
        for pos in dir:
            if pos == (r, c):
                print(result)
                return
            else:
                result += 1
    for ci, cj in dir:
        if ci <= r < ci + 2 ** (n - 1) and cj <= c < cj + 2 ** (n - 1):
            dfs(ci, cj, r, c, n - 1)
            return
        else:
            result += 2 ** (2 * n - 2)

result = 0
dfs(0, 0, r, c, N)