#include<iostream>
#include<string>

using namespace std;

auto solution() {
	long long k;

	cin >> k;
	k -= 1;

	while (k >= 0) {
		// K:홀수
		if (k % 2 == 1) {
			k = (k - 1) / 2;
		}
		// K:짝수
		if (k % 4 == 0) {
			return 0;
		}
		else if(k % 2 == 0){
			return 1;
		}
	}
	return 0;
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
		int answer = solution();
		cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}