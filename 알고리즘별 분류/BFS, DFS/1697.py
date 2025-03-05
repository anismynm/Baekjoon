## 메모리 초과 issue
from collections import deque
import math
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visit_dict = {N:0}
visit_stack = deque([N])

while K not in visit_dict:
    curr = visit_stack.popleft()
    sec = visit_dict[curr] + 1
    if curr + 1 not in visit_dict:
        visit_dict[curr + 1] = sec
        visit_stack.append(curr + 1)
    if curr - 1 not in visit_dict and curr >= 1:
        visit_dict[curr - 1] = sec
        visit_stack.append(curr - 1)
    if curr * 2 not in visit_dict and curr < math.ceil(2/3 * K):
        visit_dict[curr * 2] = sec
        visit_stack.append(curr * 2)

print(visit_dict[K])