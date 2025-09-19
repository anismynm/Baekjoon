N, game = input().split()
names = set()

for _ in range(int(N)):
    names.add(input())

if game == 'Y':
    print(len(names))
elif game == 'F':
    print(len(names) // 2)
else: # O
    print(len(names) // 3)