import sys
stringlist = []

count = int(input())

for i in range(count):
    paren = sys.stdin.readline().strip('\n')
    for j in range(len(paren)):
        if paren[j] == '(':
            stringlist.append(0)
        else:
            if (0 in stringlist):
                stringlist.remove(0)
            else:
                stringlist.append(1)
    if (stringlist):
        print("NO")
    else:
        print("YES")
    stringlist.clear()