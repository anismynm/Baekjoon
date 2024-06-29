T = int(input())

result = []
for _ in range(T):
    h, w, n = map(int, input().split())
    if n % h == 0:
        floor = h
        room = n // h
    else:
        floor = n % h
        room = (n // h) + 1
    
    result.append(100 * floor + room)

for i in result:
    print(i)