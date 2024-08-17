#include <stdio.h>
#include <string.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
    int result;
    char word[100];
    scanf("%s", &word);

    for (int i = 0; i < strlen(word)/2; i++) {
        if (word[i] == word[strlen(word)-i-1]) {
            result = 1;
        }
        else {
            result = 0;
            goto END;
        }
    }
    END:
        switch(result) {
            case 0:
                printf("0\n");
                break;
            case 1:
                printf("1\n");
                break;
        }
    return 0;
}