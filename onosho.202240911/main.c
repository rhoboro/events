#include <stdio.h>

int main() {
    int i = 1;
    while (i) {
        printf("整数を入力してください(0で終了): ");
        scanf("%d", &i);
        if (i > 0) {
            printf("%dは正の数です\n", i);
        } else {
            printf("%dは負の数です\n", i);
        }
    }
    return 0;
}
