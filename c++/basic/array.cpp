#include <stdio.h>

int main(void) {
	int arr[4];

	for (register int i = 0; i < 4; i++) {
		arr[i] = i + 1;
	}

	int twoDimArr[2][4];

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 4; j++) {
			twoDimArr[i][j] = (i * 4) + (j + 1);
		}
	}

	for (register int i = 0; i < 2; i++) {
		for (register int j = 0; j < 4; j++) {
			printf("%d ", twoDimArr[i][j]);
		}
		printf("\n");
	}

	return 0;
}