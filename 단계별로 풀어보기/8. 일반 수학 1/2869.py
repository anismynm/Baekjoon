A, B, V = list(map(int, input().split()))

result = (V - A) // (A - B)
if (V - A) % (A - B) == 0:
    result += 1
else:
    result += 2

print(result)