num_list = list(map(int, input().split()))
a = num_list[0]
b = num_list[1]
c = num_list[2]

if (a == b) and (b == c):
    print(10000 + (1000 * a))
elif (a == b) and (a != c):
    print(1000 + (100 * a))
elif (b == c) and (a != b):
    print(1000 + (100 * b))
elif (a == c) and (a != b):
    print(1000 + (100 * a))
elif (a != b) and (b != c) and (c != a):
    print(max(num_list) * 100)
