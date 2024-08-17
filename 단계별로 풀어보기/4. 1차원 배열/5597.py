std_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(28):
    a = int(input())
    std_list[a-1] = a

print(std_list.index(0) + 1)
std_list.remove(0)
print(std_list.index(0) + 2)