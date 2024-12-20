import sys
input = sys.stdin.readline

n = int(input())
atoz = 'abcdefghijklmnopqrstuvwxyz'
input_string = input().rstrip()
result = 0

for i, char in enumerate(input_string):
    result += (atoz.index(char) + 1) * 31 ** i

print(result % 1234567891)