#include<iostream>
#include<deque>
#include<unordered_map>
#include<cstring>

using namespace std;

int n, m;
int price[101];
int car[2001];
bool parking[101];
deque<int> wait;
unordered_map<int, int> um;

auto findEmpty() {
	register int i;
	bool isEmpty = false;

	for (i = 1; i <= n; i++)
	{
		if (parking[i] == false) {
			isEmpty = true;
			break;
		}
	}
	
	return isEmpty ? i : -1;
}

auto solution() {
	int carNum, cost = 0;
	register int i;

	// INIT
	memset(parking, false, sizeof(parking));
	wait.clear();
	um.clear();

	cin >> n >> m;

	for (i = 1; i <= n; i++)
		cin >> price[i];
	for (i = 1; i <= m; i++)
		cin >> car[i];
	
	for (i = 0; i < 2 * m; i++)
	{
		cin >> carNum;

		// IN
		if (carNum > 0) {
			int idx = findEmpty();
			if (idx > 0) {
				parking[idx] = true;
				cost += price[idx] * car[carNum];
				um.insert({ carNum, idx });
			}
			else {
				wait.push_back(carNum);
			}
		}
		// OUT
		else {
			int idx = um.find(-carNum)->second;
			parking[idx] = false;

			if (wait.empty() == false) {
				int idx = findEmpty();
				int carNum = wait.front();
				wait.pop_front();
				parking[idx] = true;
				cost += price[idx] * car[carNum];
				um.insert({ carNum, idx });
			}
		}
	}

	return cost;
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
		int answer = solution();
		cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}