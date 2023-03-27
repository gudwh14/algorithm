#include<iostream>
#include<string>
#include<cstring>

using namespace std;
int N, V, l, r;
string e;

int tree[1001][3];
double value[1001];
char op[1001];

int in_order(int vertex) {
	if (value[vertex] == 0) { // 해당 정점이 연산자 일 경우
		switch (op[vertex])
		{
		case '+':
			return in_order(tree[vertex][0]) + in_order(tree[vertex][1]);
			break;
		case '-':
			return in_order(tree[vertex][0]) - in_order(tree[vertex][1]);
			break;
		case '*':
			return in_order(tree[vertex][0]) * in_order(tree[vertex][1]);
			break;
		case '/':
			return in_order(tree[vertex][0]) / in_order(tree[vertex][1]);
			break;
		default:
			break;
		}
	}
	else {
		return value[vertex];
	}
}

auto solution() {
	register int i;

	// INIT
	memset(value, 0, sizeof(value));
	memset(op, ' ', sizeof(op));
	for (i = 1; i <= 1000; i++)
	{
		memset(tree[i], 0, sizeof(tree[i]));
	}

	cin >> N;
	for (i = 0; i < N; i++)
	{
		cin >> V >> e;

		if (isdigit(e[0]) == 0) { // 문자이면
			op[V] = e[0];
			cin >> l >> r;
			tree[V][0] = l;
			tree[V][1] = r;
			tree[l][2] = V;
			tree[r][2] = V;
		}
		else { // 숫자일경우
			value[V] = stoi(e);
		}
		
	}

	return in_order(1);
}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	register int test_case;

	for (test_case = 1; test_case <= 10; ++test_case)
	{
		int answer = solution();
		cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}