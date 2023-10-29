#include <stdio.h>

void clock(int gear[4][8], int n) {
    int temp = gear[n][7];
    
    for (int i = 6; i >= 0; i --) {
        gear[n][i + 1] = gear[n][i];
    }
    gear[n][0] = temp;
}

void rev_clock(int gear[4][8], int n) {
    int temp = gear[n][0];

    for (int i = 0; i < 7; i ++) {
        gear[n][i] = gear[n][i + 1];
    }
    gear[n][7] = temp;
}

void switch_gear(int gear[4][8], int cnt) {
    int gear_num, heading;

    for (int i = 0; i < cnt; i ++) {
        scanf("%d %d", &gear_num, &heading);
        int check1 = (gear[0][2] == gear[1][6]) ? 1 : 0; // check는 여기서 이미 정해짐
        int check2 = (gear[1][2] == gear[2][6]) ? 1 : 0;
        int check3 = (gear[2][2] == gear[3][6]) ? 1 : 0;

        switch (heading) {
            case 1:
            clock(gear, gear_num - 1);
            break;

            case -1:
            rev_clock(gear, gear_num - 1);
            break;
        }

        switch(gear_num) {
            case 1:
            if (check1 == 1) {
                break;
            }
            (heading == 1) ? rev_clock(gear, 1) : clock(gear, 1);
            if (check2 == 1) {
                break;
            }
            (heading == 1) ? clock(gear, 2) : rev_clock(gear, 2);
            if (check3 == 1) {
                break;
            }
            (heading == 1) ? rev_clock(gear, 3) : clock(gear, 3);
            break;

            case 2:
            if (check1 == 0) {
                (heading == 1) ? rev_clock(gear, 0) : clock(gear, 0);
            }
            if (check2 == 1) {
                break;
            }
            (heading == 1) ? rev_clock(gear, 2) : clock(gear, 2);
            if (check3 == 1) {
                break;
            }
            (heading == 1) ? clock(gear, 3) : rev_clock(gear, 3);
            break;

            case 3:
            if (check3 == 0) {
                (heading == 1) ? rev_clock(gear, 3) : clock(gear, 3);
            }
            if (check2 == 1) {
                break;
            }
            (heading == 1) ? rev_clock(gear, 1) : clock(gear, 1);
            if (check1 == 1) {
                break;
            }
            (heading == 1) ? clock(gear, 0) : rev_clock(gear, 0);
            break;

            case 4:
            if (check3 == 1) {
                break;
            }
            (heading == 1) ? rev_clock(gear, 2) : clock(gear, 2);
            if (check2 == 1) {
                break;
            }
            (heading == 1) ? clock(gear, 1) : rev_clock(gear, 1);
            if (check1 == 1) {
                break;
            }
            (heading == 1) ? rev_clock(gear, 0) : clock(gear, 0);
            break;
        }
    }
}

int get_score(int gear[4][8]) {
    int result = 0;
    for (int i = 0; i < 4; i ++) {
        if (gear[i][0] == 1) {
            result += 1 << i;
        }
    }
    return result;
}

int main() {
    int gear[4][8];
    int cnt;
    
    for (int i = 0; i < 4; i ++) {
        for (int j = 0; j < 8; j ++) {
            int temp = getchar();
            if (temp == '\n') {
                j--;
                continue;
            }
            gear[i][j] = temp - '0';
        }
    }

    scanf("%d", &cnt);
    switch_gear(gear, cnt);
    printf("%d\n", get_score(gear));

    return 0;
}