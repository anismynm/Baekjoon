#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
    int N;
    scanf("%d", &N);
    for (int i = 1; i <= N; i++) { 
        for (int j = 1; j <= N-i; j++) {
            printf(" ");
        }
        for (int k = 1; k <= 2*i-1; k++) {
            printf("*");
        }
        printf("\n");
    }
    for (int i = 1; i < N; i++) {
        for (int j = 1; j <= i; j++) {
            printf(" ");
        }
        for (int k = 1; k <= 2*N-2*i-1; k++) {
            printf("*");
        }
        if (i != N - 1) {
            printf("\n");
        }
    }

    return 0;
}