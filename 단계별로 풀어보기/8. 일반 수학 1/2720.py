T = int(input())

result = list()

for i in range(T):
    C = int(input())
    result.append(C // 25)
    C %= 25
    result.append(C // 10)
    C %= 10
    result.append(C // 5)
    C %= 5
    result.append(C // 1)


for i in range(len(result)):
    if (i != 0) & (i % 4 == 0):
        print()
    print(result[i], end = ' ')

print()