#include <iostream>
#include <stdio.h>

using namespace std;

int main(void) {
    char *name = (char*)" 차형조"; // 명시적 형변환!
    int count = strlen(name);
    printf(" %d", count);
};