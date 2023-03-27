#define _CRT_SECURE_NO_WARNINGS
#include<iostream>

using namespace std;

int code[10][7] = {
	{ 0,0,0,1,1,0,1 },
	{ 0,0,1,1,0,0,1 },
	{ 0,0,1,0,0,1,1 },
	{ 0,1,1,1,1,0,1 },
	{ 0,1,0,0,0,1,1 },
	{ 0,1,1,0,0,0,1 },
	{ 0,1,0,1,1,1,1 },
	{ 0,1,1,1,0,1,1 },
	{ 0,1,1,0,1,1,1 },
	{ 0,0,0,1,0,1,1 }
};
int arr[50][100];
int bits[56];
int num[8];

auto solution() {
	int N, M;
	register int i, j, k;
	scanf("%d %d", &N, &M);

	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			scanf("%1d", &arr[i][j]);
		}
	}

	bool flag = false;
	for (i = 0; i < N; i++) {
		for (j = M - 1; j >= 0; j--) {
			if (arr[i][j] == 1) {
				flag = true;
				for (k = 0; k < 56; k++) {
					bits[k] = arr[i][j - 55 + k];
				}
			}
			if (flag) break;
		}
	}

	for (i = 0; i < 8; i++) {
		for (k = 0; k < 10; k++) {
			bool isCorrent = true;
			for (j = 0; j < 7; j++) {
				if (bits[i * 7 + j] != code[k][j]) {
					isCorrent = false;
					break;
				}
			}
			if (isCorrent) {
				num[i] = k;
				break;
			}
		}
	}

	int odd = 0;
	int even = 0;

	for (i = 0; i < 8; i++) {
		if ((i + 1) % 2 == 0) {
			even += num[i];
		}
		else {
			odd += num[i];
		}
	}
	int total = odd * 3 + even;
	if (total % 10 == 0) {
		return odd + even;
	}
	else {
		return 0;
	}
}

int main(int argc, char** argv)
{
	int test_case;
	int T, answer;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		answer = solution();
		cout << "#" << test_case << ' ' << answer << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}