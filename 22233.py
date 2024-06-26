import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keyword = {}
for _ in range(N):
    keyword[input().rstrip()] = 1

for _ in range(M):
    words = input().rstrip().split(',')
    for word in words:
        if keyword.get(word):
            del keyword[word]
    print(len(keyword))        