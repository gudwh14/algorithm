#include<iostream>
#include<cstring>

using namespace std;

char word[101];
int N;
int alpha_info[15];
int answer;

void DFS(int n, int wordbit) {
	if (n == N) {
		if (wordbit == 0x3ffffff) answer++;
		return;
	}

	DFS(n + 1, wordbit);
	DFS(n + 1, wordbit | alpha_info[n]);
}

auto solution() {
	register int i, j;
	answer = 0;
	cin >> N;

	for (i = 0; i < N; i++)
	{
		cin >> word;
		int len = strlen(word);
		int bit = 0;
		for (j = 0; j < len; j++)
		{
			bit = bit | (1 << (word[j] - 'a')); // a:0 기준
		}
		alpha_info[i] = bit; // 알파벳 가지고있는 정보를 비트로 저장
	}

	DFS(0, 0);
}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	register int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		solution();
		cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}