#include <stdio.h>

/**
 * @brief 
 * 자연수를 비트로 변환하기
 * @param n 
 */
void printBits(int n) {
    for (int i = 7; i >=0; --i) {
        // n & (1 << i) : n의 i번쨰 비트가 1인지 아닌지 판단 가능 
        if (n & (1 << i)) printf("1");
        else printf("0");
    }
}

void printBits(long long n) {
    for (int i = 31; i >=0; --i) {
        // n & (1 << i) : n의 i번쨰 비트가 1인지 아닌지 판단 가능 
        if (n & (1 << i)) printf("1");
        else printf("0");
    }
}

/**
 * @brief 
 * Bit를 이용한 부분집합 생성 코드
 * @param arr 
 * @param n 
 */
void printSubsets(char arr[], int n) {
    for (int i = 0; i < (1 << n); i++) {
        printf("{");
        for (int j = 0; j <= n; j++) {
            if (i & (1 << j)) printf("%c", arr[j]);
        }
        printf("}\n");
    }
}

/**
 * @brief 
 * 영문자 대,소문자 변환
 * @param string 
 * @return char 
 */
char caseConvert(char alphabet) {
    return alphabet ^ 32; // 32값 -> 2^5 비트만 on/off
}

/**
 * @brief 
 * 대문자로만 이루어진 문자열 압축
 * @param str 
 * @return long long 
 */
long long compress(char str[13]) {
    long long res = 0;

    for (size_t i = 0; i < 12; i++) {
        if (str[i] == '\0') break; // 문자열이 끝이면 종료!
        res = (res << 5) | (str[i] ^ 64); // 기존 res를 앞으로 5칸 밀고 str[i] 압축하기
    }
    return res;
}

int main(int argc, char** argv) {
    // NUMBER To BIT
    for (char i = 0; i < 6; i++) {
        printf("%3d = ", i);
        printBits(i);
        printf("\n");
    }

    // MAKE SUBSET
    char data[] = { 'A', 'B', 'C', 'D'};
    printSubsets(data, 4);

    // CASE CONVERT
    printf("%c\n", caseConvert('A'));

    // STRING COMPRESSION
    char *name = (char *)"GALAXY";
    printBits(compress(name));

    return 0;
}