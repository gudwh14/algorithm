#include <iostream>
#include <set>

using namespace std;

int main() {
	// 0. INIT
	set<int> s;
	set<int> s2 = { 10, 20, 30 };

	pair<set<int>::iterator, bool> ret; // first: iter, seconde: insert 성공 여부

	// 1. DATA INSERT
	ret = s.insert(10); // VALUE 삽입
	cout << ret.second << endl;
	ret = s.insert(10); // VALUE 삽입
	cout << ret.second << endl;
	
	set<int>::iterator iter = s.begin();
	iter = s.insert(iter, 2); // ITER 위치에 VALUE 삽입

	// 2. DATA 참조
	s.find(2);

	// 3. DATA REMOVE
	s.erase(2);
	iter = s2.begin();
	s2.erase(iter);

	// 4. BOUND
	set<int>::iterator lower;
	set<int>::iterator upper;
	
	lower = s.lower_bound(10);
	upper = s.upper_bound(20);

	s.erase(lower, upper); // 10 ~ 20 사이 지우기
}