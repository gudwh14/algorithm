#include<iostream>
#include <cstring>

using namespace std;

int V, E, v1, v2, parent, child;
int tree[10001][3]; // 0: left, 1: right, 2: parent
bool visit[10001];
int result;

void order(int vertex) {
	if (tree[vertex][0] != 0) {
		order(tree[vertex][0]);
	}

	if (tree[vertex][1] != 0) {
		order(tree[vertex][1]);
	}
	result++;
}

auto solution() {
	register int i;
	cin >> V >> E >> v1 >> v2;

	// INIT
	result = 0;
	for (i = 1; i <= V; i++)
	{
		memset(tree[i], 0, sizeof(tree[i]));
	}
	memset(visit, false, sizeof(visit));

	// tree making;
	for (i = 0; i < E; i++)
	{
		cin >> parent >> child;
		if (tree[parent][0] == 0) {
			tree[parent][0] = child;
		}
		else {
			tree[parent][1] = child;
		}
		tree[child][2] = parent;
	}

	while (tree[v1][2] != 0) {
		visit[tree[v1][2]] = true;
		v1 = tree[v1][2];
	}

	int v2_parent;
	while (true) {
		v2_parent = tree[v2][2];
		if (visit[v2_parent] == true) break;
		v2 = v2_parent;
	}
	order(v2_parent);
	
	return v2_parent;
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
		cout << '#' << test_case << ' ' << answer << ' ' << result << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}