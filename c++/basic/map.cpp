#include<iostream>
#include<string>
#include<unordered_map>

using namespace std;

void printMap(unordered_map<string, int> umap) {
	for (auto i: umap)
	{
		cout << "key :" << i.first << " value :" << i.second << endl;
	}
}

int main() {
	// 0. INIT
	unordered_map<string, int> umap;
	unordered_map<string, int>::iterator iter = umap.begin();

	// 1. DATA INSERT
	umap.insert({ "key", 1 });
	umap["index"] = 2;

	// 2. DATA 참조
	cout << umap["key"] << endl;

	printMap(umap);

	for (iter = umap.begin(); iter != umap.end(); iter++)
	{
		cout << iter->first << iter->second << endl;
	}

	iter = umap.find("key");

	// 3. DATA REMOVE
	umap.erase(iter);
	umap.erase("index");
	umap.clear();
}