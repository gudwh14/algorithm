#define _CRT_SECURE_NO_WARNINGS

#include<cstring>
#include<iostream>
#include<map>
#include<string>

using namespace std;

map<string, int> num = {
	{"ZRO", 0 },
	{"ONE", 1 },
	{"TWO", 2 },
	{"THR", 3 },
	{"FOR", 4 },
	{"FIV", 5 },
	{"SIX", 6 },
	{"SVN", 7 },
	{"EGT", 8 },
	{"NIN", 9 },
};
map<int, string> numToString = {
	{0, "ZRO"},
	{1, "ONE"},
	{2, "TWO"},
	{3, "THR"},
	{4, "FOR"},
	{5, "FIV"},
	{6, "SIX"},
	{7, "SVN"},
	{8, "EGT"},
	{9, "NIN"},
};
int counts[10];

auto solution() {
	string testCase;
	int len;
	memset(counts, 0, sizeof(counts));
	cin >> testCase >> len;
	for (size_t i = 0; i < len; i++)
	{
		string temp;
		cin >> temp;
		int idx = num[temp];
		counts[idx] += 1;
	}

	cout << testCase << endl;
	for (size_t i = 0; i < 10; i++)
	{
		for (int j = 0; j < counts[i]; j++) {
			cout << numToString[i] << " ";
		}
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
		solution();
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}