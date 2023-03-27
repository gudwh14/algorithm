#include<iostream>

using namespace std;

char arr[8][8];

auto printBoard() {
	register int i, j;
	for (i = 0; i < 8; i++)
	{
		for (j = 0; j < 8; j++)
		{
			cout << arr[i][j];
		}
		cout << endl;
	}
}

auto solution() {
	int len;
	register int i, j;
	int count = 0;

	cin >> len;
	for (i = 0; i < 8; i++)
	{
		for (j = 0; j < 8; j++)
		{
			cin >> arr[i][j];
		}
	}

	// 가로 팰린드롬 찾기
	for (i = 0; i < 8; i++)
	{
		for (j = 0; j <= 8 - len; j++) {
			// 홀수 , 짝수
			bool isPalindrom = true;
			for (register int k = 0; k < len / 2; k++)
			{
				if (arr[i][j + k] != arr[i][j + len - 1 - k]) {
					isPalindrom = false;
					break;
				}
			}
			if (isPalindrom) {
				count += 1;
				//cout << "yes :" << i << ", " << j << endl;
			}
				
		}
	}

	// 세로 팰린드롬 찾기
	for (j = 0; j < 8; j++)
	{
		for (i = 0; i <= 8 - len; i++) {
			// 홀수 , 짝수
			bool isPalindrom = true;
			for (register int k = 0; k < len / 2; k++)
			{
				if (arr[i + k][j] != arr[i + len - 1 - k][j]) {
					isPalindrom = false;
					break;
				}
			}
			if (isPalindrom) {
				count += 1;
				//cout << "yes :" << i << ", "<< j<< endl;
			}

		}
	}

	return count;
}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int test_case;

	for (test_case = 1; test_case <= 10; ++test_case)
	{
		int answer;
		answer = solution();
		cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}