#include<iostream>
#include<algorithm>

using namespace std;

int buildings[1000];

int solution() {
	int answer = 0;
	int N;
	register int i;
	
	cin >> N;

	for (i = 0; i < N; i++) {
		cin >> buildings[i];
	}

	for (i = 2; i < N - 2; i++) {
		// find left
		int now = buildings[i];
		int left_1 = now - buildings[i - 1];
		int left_2 = now - buildings[i - 2];
		int right_1 = now - buildings[i + 1];
		int right_2 = now - buildings[i + 2];
		if (left_1 > 0 && left_2 > 0 && right_1 > 0 && right_2 > 0) {
			answer += min(min(left_1, left_2), min(right_1, right_2));
		}
	}
	return answer;
}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int test_case;
	for (test_case = 1; test_case <= 10; ++test_case)
	{
		int result = solution();
		cout << '#' << test_case << ' ' << result << endl;
	}
	return 0;
}