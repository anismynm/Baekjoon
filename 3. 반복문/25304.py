cost_count_list = []
X = int(input())
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    cost_count_list.append(a)
    cost_count_list.append(b)
sum = 0
for i in range(0, 2 * N, 2):
    sum += (cost_count_list[i] * cost_count_list[i + 1])

if sum == X:
    print("Yes")
else:
    print("No")