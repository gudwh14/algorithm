#include <iostream>
#include <queue>

using namespace std;

int main() {
	// 0. INIT
	queue<int> q;


	// 1. DATA INSERT 
	for (size_t i = 0; i < 5; i++)
	{
		q.push(i); // queue 삽입
	}

	// 2. DATA 참조
	q.front();
	q.back();

	// 3. DATA 삭제
	for (size_t i = 0; i < 5; i++)
	{
		cout << q.front() << endl;
		q.pop(); // q[0] 삭제
	}

	// 4. QUEUE SIZE
	q.size();
	q.empty();
}