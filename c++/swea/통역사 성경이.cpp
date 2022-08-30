#include<iostream>
#include<string>
#include<cctype>

using namespace std;

auto solution(int test_case) {
	int N;
	cin >> N;

	int idx = 0;
	string sentense;
	register int i;
	int len;
	int count[5] = { 0, 0, 0, 0, 0};

	cout << '#' << test_case << ' ';

	while (idx < N) {
		bool isEnd = false;
		cin >> sentense;
		len = sentense.size();

		if (sentense[len - 1] == '.' || sentense[len - 1] == '?' || sentense[len - 1] == '!') {
			isEnd = true;
		}
		if (islower(sentense[0]) || !isalpha(sentense[0])) {
			if (isEnd)
				idx += 1;
			continue;
		}

		bool isName = true;
		if (isEnd) {
			for (i = 1; i < len - 1; i++)
			{
				if (isupper(sentense[i]) || !isalpha(sentense[i])) {
					isName = false;
					break;
				}
			}
		}
		else {
			for (i = 1; i < len; i++)
			{
				if (isupper(sentense[i]) || !isalpha(sentense[i])) {
					isName = false;
					break;
				}
			}
		}

		if (isName)
			count[idx] += 1;

		if (isEnd)
			idx += 1;
	}

	for (i = 0; i < N; i++)
	{
		cout << count[i] << ' ';
	}
	cout << endl;
}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		solution(test_case);
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}