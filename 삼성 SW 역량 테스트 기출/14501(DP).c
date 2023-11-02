#include <stdio.h>

typedef struct {
    int time;
    int profit;
} Work;

int main() {
    int N;
    scanf("%d", &N);

    Work works[N];
    int dp[N + 1]; // 각 날짜별 최대 이익을 저장하는 배열

    for (int i = 0; i < N; i++) {
        scanf("%d %d", &works[i].time, &works[i].profit);
    }

    for (int i = 0; i <= N; i++) {
        dp[i] = 0;
    }

    for (int i = 0; i < N; i++) {
        int nextDay = i + works[i].time;
        if (nextDay <= N) {
            dp[nextDay] = dp[nextDay] > dp[i] + works[i].profit ? dp[nextDay] : dp[i] + works[i].profit;
        }
        dp[i + 1] = dp[i + 1] > dp[i] ? dp[i + 1] : dp[i];
    }

    printf("%d\n", dp[N]);

    return 0;
}
