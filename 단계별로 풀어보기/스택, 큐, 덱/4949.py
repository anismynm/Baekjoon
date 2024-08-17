import sys
input = sys.stdin.readline
parenlist = []
resultlist = []

while True:
    stringlist = input().rstrip()
    if stringlist == '.':
        break

    for str in stringlist:
        if str == '(':
            parenlist.append(0)
        elif str == '[':
            parenlist.append(2)
        elif str == ')':
            if parenlist and parenlist[-1] == 0:
                parenlist.pop()
            else:
                parenlist.append(0)
                break
        elif str == ']':
            if parenlist and parenlist[-1] == 2:
                parenlist.pop()
            else:
                parenlist.append(0)
                break          
        else:
            continue

    if parenlist:
        resultlist.append("no")
    else:
        resultlist.append("yes")
    parenlist.clear()

for i in resultlist:
    print(i)