vowels = ['a', 'e', 'i', 'o', 'u']
while True:
    word = input()
    if word == 'end':
        break
    
    flag = False
    vowel = False
    cons_cnt = vowel_cnt = 0
    for i in range(len(word)):
        w = word[i]

        if not vowel and w in vowels:
            vowel = True

        if w in vowels:
            cons_cnt = 0
            vowel_cnt += 1
        else:
            cons_cnt += 1
            vowel_cnt = 0
        
        if cons_cnt == 3 or vowel_cnt == 3:
            flag = True
            break

        if i != len(word) - 1 and w != 'e' and w != 'o' and w == word[i + 1]:
            flag = True
            break
        
    if flag or not vowel:   
        print(f'<{word}> is not acceptable.')
    else:
        print(f'<{word}> is acceptable.')