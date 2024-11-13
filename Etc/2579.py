n = int(input())
stair = [0]
dp = [0]

for _ in range(n):
    stair.append(int(input()))

if n >= 1:
    dp.append(stair[1])
if n >= 2:
    dp.append(stair[1] + stair[2])
if n >= 3:
    dp.append(max(stair[1], stair[2]) + stair[3])

for i in range(4, n + 1):
    dp.append(max(dp[-3] + stair[i - 1], dp[-2]) + stair[i])

print(dp[-1])