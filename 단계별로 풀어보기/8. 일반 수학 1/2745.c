#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
    int B;
    int result = 0;
    char N[30];

    scanf("%s %d", N, &B);
    
    for (int i = 0; i < strlen(N); i ++) {
        if (N[i] >= 48 && N[i] <= 57) {
            result += (int)pow(B, strlen(N) - i - 1) * (N[i] - 48);
        }
        else {
            result += (int)pow(B, strlen(N) - i - 1) * (N[i] - 55);
        }
    }

    printf("%d\n", result);
}