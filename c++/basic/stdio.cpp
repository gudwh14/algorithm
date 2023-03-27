#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int T, r, c;
	char arr[100][100];

	scanf("%d", &T);
	scanf("%d %d", &r, &c);

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			scanf("%c", &arr[i][j]);
		}
	}

	printf("%d, %d, %d\n", T, r, c);

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			printf("%c", arr[i][j]);
		}
		printf("\n");
	}
}
