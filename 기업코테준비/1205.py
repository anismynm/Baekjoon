N, new_score, P = map(int, input().split())
if N == 0:
    print(1)
    exit()
score_list = list(map(int, input().split()))

i = 0
rank = 1
while i < P and i < len(score_list):
    if i != 0 and score_list[i] != score_list[i - 1]:
        rank = i + 1
    
    if score_list[i] > new_score:
        i += 1
        if i == len(score_list) and i < P:
            print(i + 1)
            exit()
    elif score_list[i] == new_score:
        i += 1
        if i < P and (i == len(score_list) or score_list[i] != new_score):
            print(rank)
            exit()
    else:
        print(rank)
        exit()

print(-1)