#include<iostream>
#include<vector>
#include<algorithm>
#include <cstring>
#include<cmath>

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
int N, x, y;
double E;
vector<pair<ll, pii>> graph;
int graph_x[1000];
int graph_y[1000];
int parent[1000];

int findParent(int x) {
	if (x != parent[x]) {
		parent[x] = findParent(parent[x]);
	}

	return parent[x];
}

bool unionParent(int a, int b) {
	int parent_a = findParent(a);
	int parent_b = findParent(b);

	if (parent_a != parent_b) {
		if (a < b) parent[parent_b] = parent_a;
		else parent[parent_a] = parent_b;
		return true;
	}
	else {
		return false;
	}
}

void init() {
	graph.clear();
}

auto solution() {
	register int i, j;
	ll cost = 0;
	int count = 0;
	cin >> N;

	for (i = 0; i < N; i++)
	{
		cin >> x;
		graph_x[i] = x;
		parent[i] = i;
	}
	for (i = 0; i < N; i++)
	{
		cin >> y;
		graph_y[i] = y;
	}
	cin >> E;
	for (i = 0; i < N; i++)
	{
		ll _x = graph_x[i], _y = graph_y[i];

		for (j = i + 1; j < N; j++)
		{
			ll t_x = graph_x[j], t_y = graph_y[j];
			ll distance = (_x - t_x) * (_x - t_x) + (_y - t_y) * (_y - t_y);
			//cout << i << ", " << j << " : " << " _x: " << _x << " _y: " << _y << " t_x: " << t_x << " t_y: " << t_y << " -> " << distance << endl;
			graph.push_back({ distance, {i, j}});
		}
	}
	sort(graph.begin(), graph.end());

	for (auto i:graph)
	{
		if (count == N - 1) break;
		if (unionParent(i.second.first, i.second.second)) {
			cost += i.first;
			count++;
			//cout << "연결: " << i.first.first << " -> " << i.first.second << " = " << i.second << endl;
		}
	}

	init();
	return round(double(cost * E));
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
		ll answer = solution();
		cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}