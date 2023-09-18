num_list = []
for i in range(10):
    a = int(input())
    mod = a % 42
    num_list.append(mod)

result = []
for j in range(len(num_list)):
    if num_list[j] not in result:
        result.append(num_list[j])

print(len(result))