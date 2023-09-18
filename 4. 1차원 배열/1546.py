n = int(input())
score_list = [float(x) for x in input().split()]
max = max(score_list)
new_score_average = (sum(score_list) / max) * (100 / n)
print(new_score_average)