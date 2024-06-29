import sys
input = sys.stdin.readline

N, M = map(int, input().split())
str_dict = {}

for _ in range(N):
    str = input().rstrip()
    if (len(str) >= M):
        if str_dict.get(str):
            str_dict[str] += 100
        else:
            str_dict[str] = 100 + len(str)

str_dict = sorted(str_dict.items())
result = sorted(str_dict, key = lambda x: x[1], reverse = True)

for elem in result:
    print(elem[0])