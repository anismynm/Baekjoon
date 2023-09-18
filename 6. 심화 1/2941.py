word = input()
length = len(word)
count = 0
for i in range(len(word)-1):
    if word[i] == 'c' and (word[i+1] == '=' or word[i+1] == '-'): #c=, c-
        count += 1
        length -= 2
    elif word[i] == 'd' and word[i+1] == '-': #d-
        count += 1
        length -= 2
    elif (word[i] == 'l' or word[i] == 'n') and word[i+1] == 'j': #lj, nj
        count += 1
        length -= 2
    elif word[i] == 's' and word[i+1] == '=': #s=
        count += 1
        length -= 2
    elif word[i] == 'z' and word[i+1] == '=': #z=
        if word[i-1] != 'd':
            count += 1
            length -= 2

for j in range(len(word)-2):
    if word[j] == 'd' and word[j+1] == 'z' and word[j+2] == '=': #dz=
        count += 1
        length -= 3

print(count+length)