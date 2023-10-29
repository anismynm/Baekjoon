#include <stdio.h>

int main() {
    int iInput;
    int max = 0;
    int max_row = 1;
    int max_column = 1;

    for (int i = 0; i < 9; i ++) {
        for (int j = 0; j < 9; j ++) {
            scanf("%d", &iInput);
            if (iInput > max) {
                max = iInput;
                max_row = i + 1;
                max_column = j + 1;
            }
        }
    }

    printf("%d\n%d %d\n", max, max_row, max_column);
    return 0;
}