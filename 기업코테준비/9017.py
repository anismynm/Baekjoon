import sys
input = sys.stdin.readline
INF = int(1e6)

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    rank = list(map(int, input().split()))
    maxTeamNum = max(rank)

    teamCnt = [-1]
    scoreSum = [[INF, INF, -1]]
    for i in range(1, maxTeamNum + 1):
        cnt = rank.count(i)
        teamCnt.append(cnt)
        scoreSum.append([0, 0, i]) if cnt == 6 else scoreSum.append((INF, INF, i))

    score = 1
    finishCnt = [0] * (maxTeamNum + 1)
    for team in rank:
        if teamCnt[team] == 6:
            if finishCnt[team] < 4:
                scoreSum[team][0] += score
            elif finishCnt[team] == 4:
                scoreSum[team][1] += score
            score += 1
        finishCnt[team] += 1

    scoreSum = sorted(scoreSum, key = lambda x:(x[0], x[1]))
    result.append(scoreSum[0][2])

for i in result:
    print(i)