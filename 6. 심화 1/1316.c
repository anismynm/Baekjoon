#include <stdio.h>
#include <string.h>

int main() {
    int result = 0;
    char word[100];
    int cnt;
    int atoz[26];
    scanf("%d", &cnt);

    for (int i = 0; i < cnt; i ++) {
        for (int p = 0; p < 26; p ++) {
            atoz[p] = 0;
        }

        scanf("%s", word);
        int length = 0;
        while (word[length] != '\0') {
            length++;
        }
        atoz[(int)word[0] - 97]++;

        if (length <= 2) {
            result++;
        }
        else {
            for (int j = 1; j < length; j ++) {
                int index = (int)word[j] - 97;

                if (atoz[index] > 0 && word[j - 1] != word[j]) { 
                    break;
                }
                else {
                    atoz[index]++;

                    if (j == length - 1) {
                        result++;
                    }
                }
            }
        }
        
    }

    printf("%d\n", result);

    return 0;
}