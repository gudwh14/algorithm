#include <stdio.h>

auto printArr(int arr[], int size) {
	for (register int i = 0; i < size; i++) {
		printf("%d ", arr[i]);
	}
	printf("\n");
}

auto bubbleSort(int arr[], int size) {
	for (register int i = size - 1; i > 0; i--) {
		for (register int j = 0; j < i; j++) {
			if (arr[j] > arr[j + 1]) {
				int temp = arr[j + 1];
				arr[j + 1] = arr[j];
				arr[j] = temp;
			}
		}
	}
}

auto insertSort(int arr[], int size) {
	register int i, j;

	for (i = 1; i < size; i++) {
		for (j = 0; j < i; j ++) {
			if (arr[i] < arr[j]) {
				int temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		}
	}
}

auto selectSort(int arr[], int size) {
	register int i, j;

	for (i = 0; i < size; i++) {
		int minValue, minIndex = arr[i], i;
		for (j = i + 1; j < size; j++) {
			if (minValue < arr[j]) {
				minValue = arr[j];
				minIndex = j;
			}
		}
		if (arr[i] != minValue) {
			int temp = arr[i];
			arr[i] = minValue;
			arr[minIndex] = temp;
		}
	}
}

int main(void) {
	int arr[5] = { 5, 1, 2, 3, 4 };
	int size = sizeof(arr) / sizeof(int);

	printArr(arr, size);
	bubbleSort(arr, 5);
	insertSort(arr, 5);
	selectSort(arr, 5);
	printArr(arr, size);
}