#include<iostream>

using namespace std;

int list1[7] = { 1, 2, 5, 10, 20, 25, 50 };
int list2[5] = { 100, 125, 200, 250, 500 };
auto solution() {
	int X;
	cin >> X;

	register int i, j;
	int count = 0;
	
	for (i = 0; i < 7; i++)
	{
		if (list1[i] <= X) count++;
		else return count;
	}

	for (i = 1; i <= 10000000; i = i * 10)
	{
		for (j = 0; j < 5; j++)
		{
			if (list2[j] * i <= X) count++;
			else return count;
		}
	}
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
		cout << '#' << test_case << ' ' << solution() << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}