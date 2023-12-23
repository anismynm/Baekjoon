import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cir = []
togo = 0

for i in range(N):
    cir.append(i + 1)

print("<", end = "")

while(cir):
    togo = (togo + K - 1) % N
    if (len(cir) == 1):
        print(cir.pop(togo), end = "")
    else:
        print(cir.pop(togo), end = ", ")
    N -= 1

print(">")