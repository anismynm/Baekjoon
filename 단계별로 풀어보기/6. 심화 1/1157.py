N = input()
arr = []
for i in range(26):
    arr.append(0)
for i in range(len(N)):
    if ord(N[i]) >= 65 and ord(N[i]) <= 90:
        arr[ord(N[i])-65] += 1
    elif ord(N[i]) >= 97 and ord(N[i]) <= 122:
        arr[ord(N[i])-97] += 1

def arr_max(list):
    max = 0
    count = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
            max_index = i
            count = 0
        elif list[i] == max:
            count += 1
    if count != 0:
        print("?")
    else:
        print(chr(max_index+65))

arr_max(arr)