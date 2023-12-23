import sys
input = sys.stdin.readline

count = int(input())
line = list(map(int, input().rstrip().split()))
waiting = []

gift = 1
for i in range(len(line)):
    if line[0] == gift:
        line.pop(0)
        gift += 1
    else:
        if waiting:
            if waiting[-1] == gift:
                waiting.pop()
                gift += 1
            else:
                if line[0] < waiting[-1]:
                    waiting.append(line.pop(0))
                else:
                    print("Sad")
                    sys.exit()
        else:
            waiting.append(line.pop(0))

print("Nice")