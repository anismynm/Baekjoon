import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hear = []
seen = []

for _ in range(N):
    hear.append(input().rstrip())
for _ in range(M):
    seen.append(input().rstrip())

result = sorted(set(hear) & set(seen))

print(len(result))
for person in result:
    print(person)