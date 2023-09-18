C = int(input())
result = []
for i in range(C):
    score = list(map(int, input().split()))
    average = sum(score[1:]) / score[0]
    over = 0
    for i in range(1, len(score)):
        if score[i] > average:
            over += 1
    percent = (over / score[0]) * 100
    result.append(percent)

for j in range(len(result)):
    print('%.3f'%result[j],"%",sep="")
