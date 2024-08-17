from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

count = 0

for i in range(len(A) - 1, -1, -1):
    if A[i] == 0 and count < M:
        print(B[i], end = " ")
        count += 1

if count < M:
    for i in range(0, M - count):
        print(C[i], end = " ")

print()