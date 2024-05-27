from itertools import combinations
import math

N = int(input())
S = []

for i in range(N):
    S.append(list(map(int, input().split())))

divided = list(combinations(range(N), int(N/2)))
divided_S = []

# 두 집합 list로 바꾸고 두 변수로 나누고
for i in range(len(divided)//2):
    divided_S.append([list(divided[i]), list(divided[len(divided) - 1 - i])])

# 또 그 나눈 집합에서 2개 뽑는 조합 만들어서 능력치 차이 구해서 result.append
result = []
for teams in divided_S:
    score = [0, 0]
    for i, team in enumerate(teams):
        team_comb = list(combinations(team, 2))
        for comb in team_comb:
            score[i] += S[comb[0]][comb[1]] + S[comb[1]][comb[0]]
    result.append(abs(score[0] - score[1]))       

print(min(result))