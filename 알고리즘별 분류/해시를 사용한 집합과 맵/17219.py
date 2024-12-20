import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = {}

for _ in range(N):
    site, password = input().rstrip().split()
    memo[site] = password

for _ in range(M):
    print(memo.get(input().rstrip()))