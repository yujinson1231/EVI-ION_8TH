#include <stdio.h>

int main() {
    int a = 8;      // 원래는 5였던 값, 8로 변경
    int b = a - 3;  // 뺄셈 연산 추가

    if (a != b) {
        a = 0;          // FAIL 부분
    } else {
        a = a + 12;     // ADD 부분 (10에서 12로 바꿈)
    }

    printf("Result: %d\n", a);
    return 0;
}
