#include<iostream>
#include<vector>

using namespace std;

void printVectorByIter(vector<int> v) {
	vector<int>::iterator iter; // iterator는 주소값을 가르키고 있음

	for (iter = v.begin(); iter < v.end(); iter++)
	{
		cout << *iter << endl;
	}
}

void printVectorByAuto(vector<int> v) {
	for (auto i : v)
		cout << i << endl;
}

void printVectorByIndex(vector<int> v) {
	register int i;

	for (i = 0; i < v.size(); i++)
	{
		cout << v[i] << endl;
	}
}

int main() {
	// 0. Init
	vector<int> v;
	vector<int> v2(10, 3); // 크기가 10, 값이 3으로 초기화된 벡터
	vector<int> v3 = { 1, 2, 3, 4 };
	
	// 1. 데이터 넣기
	v.push_back(1); // 벡터 맨뒤에 삽입

	vector<int>::iterator iter = v.begin(); // vector<int> iter
	iter = v.insert(iter, 5); // iter 위치에 5 삽입, insert시 벡터 재할당 되어 주소값 바뀜
	cout << *iter << endl;

	// 2. 데이터 삭제
	v.pop_back(); // 맨뒤에서 데이터 삭제
	iter = v.begin();
	v.erase(iter); // iter가 가르키는 위치 삭제

	v.push_back(3);
	// 3. 데이터 접근
	v[0] = 100;
	v.at(0);
	v.front();
	v.back();

	// 4. 크기 함수
	v.size(); // 원소 갯수 반환
	v.capacity(); // 할당된 원소 갯수 반환
	v.empty();

	// 5. 응용
	vector<pair<int, int>> pairVector;
	pairVector.push_back({ 1, 2 });
	cout << pairVector[0].first << "," << pairVector[0].second << endl;
}