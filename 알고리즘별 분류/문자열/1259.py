import sys
input = sys.stdin.readline

while True:
    word = input().rstrip()
    if word == '0':
        break
    if len(word) % 2 == 0:
        if word[0:len(word)//2] == word[:len(word)//2 - 1:-1]:
            print('yes')
        else:
            print('no')
    else:
        if word[0:len(word)//2] == word[:len(word)//2:-1]:
            print('yes')
        else:
            print('no')