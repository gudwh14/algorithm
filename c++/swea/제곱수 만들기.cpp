#include <iostream>   
#include <vector>
#include <algorithm>
#include <cmath>
#define MAX 3162
using namespace std;

int p[MAX] = { 0, };
int idx;

int runDevide(int A) {
    for (int i = 0; i < idx; i++) {
        while (A % p[i] == 0) A /= p[i];
        if (A < p[i]) break;
    }

    return A;
}

void runPrime() {
    for (int i = 2; i <= MAX; i++) {
        bool flag = true;
        for (int n = 2; n < i; n++) {
            if (i % n == 0) {
                flag = false;
                break;
            }
        }

        if (flag) p[idx++] = pow(i, 2);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    setbuf(stdout, NULL);

    int T;
    cin >> T;
    
    runPrime();

    for (int t = 1; t <= T; t++) {
        int A, B;

        cin >> A;

        B = A;
        B = runDevide(B);

        cout << '#' << t << ' ' << B << '\n';
    }
    return 0;
}