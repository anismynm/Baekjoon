big_word = input()
time = 0
for i in range(len(big_word)):
    if big_word[i] == 'A' or big_word[i] == 'B' or big_word[i] == 'C': 
        time += 3
    elif big_word[i] == 'D' or big_word[i] == 'E' or big_word[i] == 'F':
        time += 4
    elif big_word[i] == 'G' or big_word[i] == 'H' or big_word[i] == 'I':
        time += 5
    elif big_word[i] == 'J' or big_word[i] == 'K' or big_word[i] == 'L':
        time += 6
    elif big_word[i] == 'M' or big_word[i] == 'N' or big_word[i] == 'O':
        time += 7  
    elif big_word[i] == 'P' or big_word[i] == 'Q' or big_word[i] == 'R' or big_word[i] == 'S':
        time += 8
    elif big_word[i] == 'T' or big_word[i] == 'U' or big_word[i] == 'V':
        time += 9
    elif big_word[i] == 'W' or big_word[i] == 'X' or big_word[i] == 'Y' or big_word[i] == 'Z':
        time += 10
print(time)