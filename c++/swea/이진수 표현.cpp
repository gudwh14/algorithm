#include<iostream>

using namespace std;

auto solution() {
	int N, M;
	register int i;
	cin >> N >> M;
	
	int temp = 0;
	int flag = true;
	for (i = 0; i < N; i++)
	{
		temp = temp | (1 << i);
		if ((M & temp) != temp) {
			flag = false;
			break;
		}
	}

	// M과 temp 비트 비교하기
	if (flag) cout << "ON" << endl;
	else cout << "OFF" << endl;

	return;
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
		cout << '#' << test_case << ' ';
		solution();
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}