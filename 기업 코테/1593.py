from itertools import permutations
import sys
input = sys.stdin.readline

w, s = map(int, input().split())
W = list(input().rstrip())
S = list(input().rstrip())
alpha_w = [0 for _ in range(52)]
alpha_s = [0 for _ in range(52)]
result = 0

for elem in W:
    if 65 <= ord(elem) <= 90:
        alpha_w[ord(elem) - 65] += 1
    else:
        alpha_w[ord(elem) - 71] += 1

for i in range(s):
    if i >= w:
        if 65 <= ord(S[i - w]) <= 90:
            alpha_s[ord(S[i - w]) - 65] -= 1
        else:
            alpha_s[ord(S[i - w]) - 71] -= 1
    if 65 <= ord(S[i]) <= 90:
        alpha_s[ord(S[i]) - 65] += 1
    else:
        alpha_s[ord(S[i]) - 71] += 1
    
    if alpha_w == alpha_s:
        result += 1

print(result)