num_list = list(map(int, input().split()))
sum = 0
for i in range(len(num_list)):
    sum += (num_list[i] * num_list[i])
result = sum % 10
print(result)
