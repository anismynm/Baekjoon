import sys
input = sys.stdin.readline

N, K = map(int, input().split())

table = list(input().rstrip())
hambugi = []
result = 0

for i in range(N):
    if table[i] == 'P':
        for j in range(max(0, i - K), min(i + K + 1, N)):
            if table[j] == 'H':
                table[j] = 'O'
                result += 1
                break

print(result)