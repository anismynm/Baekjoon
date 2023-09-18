#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int king, queen, look, vishop, knight, phone;
    scanf("%d %d %d %d %d %d", &king, &queen, &look, &vishop, &knight, &phone);
    printf("%d %d %d %d %d %d\n", 1-king, 1-queen, 2-look, 2-vishop, 2-knight, 8-phone);

    return 0;
}