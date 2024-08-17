#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
    int N, B, i = 0;
    int result[100];

    scanf("%d %d", &N, &B);
    
    while (N >= B) {
        result[i] = N % B;
        N /= B;
        i++;
    }

    if (N >= 0 && N <= 9) {
        printf("%d", N);
    }
    else {
        printf("%c", N + 55);
    }

    for (int j = i - 1; j >= 0; j --) {
        if (result[j] >= 0 && result[j] <= 9) {
            printf("%c", result[j] + 48);
        }
        else {
            printf("%c", result[j] + 55);
        }
    }
    printf("\n");
}