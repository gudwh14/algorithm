#include<iostream>
#include<vector>

using namespace std;

vector<int> Fail(string pattern) {
	int m = pattern.length();
	vector<int> pi(m); // partial match table

	pi[0] = 0;
	for (int i = 1, j = 0; i < m; i++) {
		while (j > 0 && pattern[i] != pattern[j])
			j = pi[j - 1];
		if (pattern[i] == pattern[j])
			pi[i] = ++j;
	}
	return pi;
}

int KMP(string pattern, string text) {
	int m = pattern.length();
	int n = text.length();
	vector<int> pos;
	vector<int> pi = Fail(pattern);

	for (int i = 0, j = 0; i < n; i++) {
		while (j > 0 && text[i] != pattern[j])
			j = pi[j - 1];
		if (text[i] == pattern[j]) {
			if (j == m - 1) {
				pos.push_back(i - m + 1);
				j = pi[j];
			}
			else j++;
		}
	}
	return pos.size();
}


auto solution() {
	int T;
	string text, pattern;
	vector<int> result;
	cin >> T;
	cin >> pattern;
	cin >> text;

	return KMP(pattern, text);
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