#include <stdio.h>

int main() {
    int N, M;
    int iInput;
    scanf("%d %d", &M, &N);
    int array1[N][M], array2[N][M];

    for (int i = 0; i < N; i ++) {
        for (int j = 0; j < M; j ++) {
            scanf("%d", &iInput);
            array1[i][j] = iInput;
        }
    }

    for (int i = 0; i < N; i ++) {
        for (int j = 0; j < M; j ++) {
            scanf("%d", &iInput);
            array2[i][j] = iInput;
        }
    }

    for (int i = 0; i < N; i ++) {
        for (int j = 0; j < M; j ++) {
            printf("%d", array1[i][j] + array2[i][j]);
            if (j != M - 1) { // 마지막꺼도 띄어쓰기하면 출력형식 오류.
                printf(" ");
            }
        }
        printf("\n");
    }


}