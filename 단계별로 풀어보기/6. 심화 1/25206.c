#include <stdio.h>
#include <string.h>

int main() {
    char a[50];
    double grade;
    char score[5];
    double SumScore = 0;
    double SumGrade = 0;

    for (int i = 0; i < 20; i ++) {
        scanf("%s %lf %s", a, &grade, score);
        
        if (strcmp(score, "A+") == 0) {
            SumScore += 4.5 * grade;
            SumGrade += grade;
        }
        else if (strcmp(score, "A0") == 0) {
            SumScore += 4.0 * grade;
            SumGrade += grade;
        }
        else if (strcmp(score, "B+") == 0) {
            SumScore += 3.5 * grade;
            SumGrade += grade;
        }
        else if (strcmp(score, "B0") == 0) {
            SumScore += 3.0 * grade;
            SumGrade += grade;
        }
        else if (strcmp(score, "C+") == 0) {
            SumScore += 2.5 * grade;
            SumGrade += grade;
        }
        else if (strcmp(score, "C0") == 0) {
            SumScore += 2.0 * grade;
            SumGrade += grade;
        }
        else if (strcmp(score, "D+") == 0) {
            SumScore += 1.5 * grade;
            SumGrade += grade;
        }
        else if (strcmp(score, "D0") == 0) {
            SumScore += 1.0 * grade;
            SumGrade += grade;
        }
        else if (strcmp(score, "F") == 0) {
            SumScore += 0.0 * grade;
            SumGrade += grade;
        }
        else {
            continue;
        }
    }

    printf("%lf\n", SumScore / SumGrade);
    return 0;

}