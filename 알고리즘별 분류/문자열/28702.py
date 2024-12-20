import sys
input = sys.stdin.readline

line = []
for _ in range(3):
    line.append(input().rstrip())

for i, elem in enumerate(line):
    try:
        pivot = int(elem)
        idx = i
    except:
        continue

result = pivot + 3 - idx

if result % 15 == 0:
    print('FizzBuzz')
elif result % 3 == 0 and result % 15 != 0:
    print('Fizz')
elif result % 5 == 0 and result % 15 != 0:
    print('Buzz')
else:
    print(result)