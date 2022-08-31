#include<iostream>
#include<algorithm>
#include <climits>
#include <cstring>

using namespace std;

int n, m;
int c1, c2;
int cow[500000];
int min_distance = INT_MAX;

auto binarySearach(int horse_z) {
	int left = 0, right = n - 1;
	int mid = (left + right) / 2;

	if (cow[left] > horse_z) {
		return 0;
	}

	if (cow[right] < horse_z) {
		return n - 1;
	}

	while (left <= right) {
		mid = (left + right) / 2;

		if (cow[mid] == horse_z) {
			return mid;
		}
		else if (cow[mid] < horse_z) {
			left = mid + 1;
		}
		else {
			right = mid - 1;
		}
	}

	if (cow[mid] < horse_z) {
		mid += 1;
	}

	return mid;
}

auto solution(int test_case) {
	register int i;
	int count = 0;

	cin >> n >> m;
	cin >> c1 >> c2;

	for (i = 0; i < n; i++) cin >> cow[i];
	sort(cow, cow + n);

	for (i = 0; i < m; i++) {
		int horse_z;
		cin >> horse_z;

		int min_cow_index = binarySearach(horse_z);
		int distance = abs(horse_z - cow[min_cow_index]);

		//cout << "hz: " << horse_z << " cow_idx: " << min_cow_index <<  " distance: " << distance << endl;
		if (min_cow_index < n) {
			if (min_distance > distance) {
				min_distance = distance;
				count = 1;
			}
			else if (min_distance == distance) {
				count += 1;
			}
		}

		if (min_cow_index > 0 && min_cow_index < n && cow[min_cow_index] != horse_z) {
			int _distance = abs(horse_z - cow[min_cow_index - 1]);

			if (min_distance > _distance) {
				min_distance = _distance;
				count = 1;
			}
			else if (min_distance == _distance) {
				count += 1;
			}
		}
	}
	cout << '#' << test_case << ' ' << abs(c2 - c1) + min_distance << ' ' << count << endl;
	memset(cow, 0, sizeof(int) * n);
	min_distance = INT_MAX;
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
		solution(test_case);
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}