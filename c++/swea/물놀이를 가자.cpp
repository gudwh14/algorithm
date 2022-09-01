#include <iostream>
#include <deque>
#include <climits>
#include <cstring>

using namespace std;

char arr[1000][1000];
int dist[1000][1000];
int n, m;
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };

auto solution() {
	register int i, j;
	int total = 0;
	deque<pair<int, int>> Q;

	cin >> n >> m;

	for (i = 0; i < n; i++)
		memset(dist[i], -1, sizeof(int) * m);

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			cin >> arr[i][j];
			if (arr[i][j] == 'W') {
				Q.push_back({ i, j });
				dist[i][j] = 0;
			}
		}
	}

	while (!Q.empty()) {
		auto cur = Q.front(); Q.pop_front();
		for (i = 0; i < 4; i++)
		{
			int r = cur.first + dx[i];
			int c = cur.second + dy[i];

			if (!(0 <= r && r < n && 0 <= c && c < m)) continue; // 배열 범위
			if (dist[r][c] >= 0) continue;

			dist[r][c] = dist[cur.first][cur.second] + 1;
			Q.push_back({ r, c });
		}
	}

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			if (arr[i][j] == 'L') {
				total += dist[i][j];
			}
		}
	}

	return total;
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