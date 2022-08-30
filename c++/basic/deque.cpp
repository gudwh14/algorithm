#include<iostream>
#include<deque>

using namespace std;

void printDequeByIter(deque<int> dq) {
	deque<int>::iterator iter = dq.begin();

	for (; iter < dq.end(); iter++)
	{
		cout << *iter << ' ';
	}
}

int main() {
	// 0. INIT
	deque<int> dq(10, 1);
	deque<int> dq2;

	// 1. DATA 참조
	dq.at(1);
	dq[5];
	dq.front();
	dq.back();

	// 2. DATA INSERT
	dq.push_front(0);
	dq.push_back(11);

	deque<int>::iterator iter = dq.begin();
	iter = dq.insert(iter, -5);
	printDequeByIter(dq);

	// 3. DATA REMOVE
	dq.pop_back();
	dq.pop_front();

	iter = dq.begin(); // insert, pop, erase 연산시 iter 초기화 필요!
	dq.erase(iter);
	dq.clear();

	// 4. DEQUE SIZE
	dq.size();
	dq.empty();
	
	dq.resize(5);
}