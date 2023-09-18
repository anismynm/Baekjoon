N = int(input())
result = []
for i in range(N):
    trial = input()
    combo = 0
    score = 0
    for i in range(len(trial)):
        if trial[i] == 'O':
            combo += 1
            score += combo
        else:
            combo = 0
    result.append(score)

for j in range(len(result)):
    print(result[j])