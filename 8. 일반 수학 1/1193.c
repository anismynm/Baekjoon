#include <stdio.h>

int main() {
    int row = 1, column, i = 1;
    scanf("%d", &column);

    while(column - i > 0) {
        column -= i;
        i++;
        row++;
    } 

    if (row % 2 == 1) {
        printf("%d/%d\n", row - column + 1, column);
    }
    else {
        printf("%d/%d\n", column, row - column + 1);
    }

    return 0;
}