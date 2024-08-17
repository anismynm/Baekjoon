S = input()
atoz = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(atoz)):
    if atoz[i] in S:
        print(S.index(atoz[i]), end = ' ')
    else:
        print("-1", end = ' ')
print("\n")