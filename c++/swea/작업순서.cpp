#include<iostream>
#include<vector>
#include<queue>
#include<cstring>

using namespace std;
int V, E;
vector<int> graph[1001];
queue<int> start, Q;
int indegree[1001];

auto solution(int test_case) {
	register int i;

	cin >> V >> E;
	for (i = 0; i < E; i++)
	{
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		indegree[v]++;
	}

	for (i = 1; i <= V; i++)
	{
		if (indegree[i] == 0) start.push(i);
	}

	cout << '#' << test_case << ' ';
	int len = start.size();
	while (!start.empty())
	{
		Q.push(start.front());
		cout << start.front() << ' ';
		start.pop();

		while (!Q.empty()) {
			int vertex = Q.front(); Q.pop();

			for (auto adjacent: graph[vertex])
			{
				indegree[adjacent]--;
				if (indegree[adjacent] == 0) {
					Q.push(adjacent);
					cout << adjacent << ' ';
				}
			}
		}
	}
	cout << endl;

	// INIT
	memset(indegree, 0, sizeof(int) * V);
	for (i = 1; i <= V; i++)
	{
		graph[i].clear();
	}

}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	register int test_case;

	for (test_case = 1; test_case <= 10; ++test_case)
	{
		solution(test_case);
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}