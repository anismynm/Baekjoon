#include <stdio.h>

void divide(int *x) {
    int div = 2;
    while (div != *x) {
        if (*x % div == 0) {
            printf("%d\n", div);
            *x /= div;
            break;
        }
        else {
            div++;
        }
    }

    if (div == *x) {
        printf("%d\n", div);
        *x /= div;
    }
}

int main() {
    int N;
    scanf("%d", &N);

    while (N != 1) {
        divide(&N);
    }
}