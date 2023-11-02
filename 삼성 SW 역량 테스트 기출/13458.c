#include <stdio.h>

int main() {
    int N, B, C;
    long long result = 0; // int 형으로는 범위 다 담을 수 없음.
    scanf("%d", &N);
    int A[N];
    for (int i = 0; i < N; i ++) {
        scanf("%d", &A[i]);
    }
    scanf("%d %d", &B, &C);

    result += N;

    for (int i = 0 ; i < N; i ++) {
        if (A[i] - B > 0) {
            result += (A[i] - B) / C;
            if ((A[i] - B) % C != 0) {
                result += 1;
            }
        }
    }
    printf("%lld\n", result);
}