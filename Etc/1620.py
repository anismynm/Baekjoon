import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokedex = {}

for i in range(N):
    name = input().rstrip()
    pokedex[name] = str(i + 1)
    pokedex[str(i + 1)] = name

for i in range(M):
    print(pokedex.get(input().rstrip()))