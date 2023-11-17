#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int arr[N];
    for (int i = 0; i < N; i ++) {
        scanf("%d", &arr[i]);
    }

    int result[N];
    int resnum = 0;
    for (int i = 0; i < N; i ++) {
        int min;
        for (int j = 0; j < N - 1; j ++) {
            if (arr[j] < ) {
                min = arr[j];
                arr[j] = 1000000001;
            }
        }
        printf("%d\n", min);
        
    }
    /*
    for (int i = 0; i < N; i ++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    */
}