#include<iostream>
#include<string>
#include<cstring>

using namespace std;

int N, v, l, r;
char ch;
int tree[101][2];
char value[101];
string str;

void in_order(int vertex) {
	if(tree[vertex][0] != 0) in_order(tree[vertex][0]);
	cout << value[vertex];
	if (tree[vertex][1] != 0) in_order(tree[vertex][1]);
	return;
}

auto solution() {
	register int i;
	cin >> N;

	for (size_t i = 0; i < 100; i++)
	{
		memset(tree[i], 0, sizeof(tree[i]));
	}
	memset(value, ' ', sizeof(value));

	for (i = 0; i < N; i++)
	{
		cin >> v >> ch;
		if (cin.get() != '\n') {
			cin >> l;
			tree[v][0] = l;
			if (cin.get() != '\n') {
				cin >> r;
				tree[v][1] = r;
			}
		}
		value[v] = ch;
	}
	in_order(1);
	cout << endl;
}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	register int test_case;

	for (test_case = 1; test_case <= 10; ++test_case)
	{
		cout << '#' << test_case << ' ';
		solution();
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}