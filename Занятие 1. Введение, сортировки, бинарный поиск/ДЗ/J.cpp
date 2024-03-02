#include <iostream>

using namespace std;

long long n, m, t;
int main() {
    cin >> t;
    for (int k = 0; k < t; k++) {
        cin >> n >> m;
        long long best = 1e18;
        char x = 'V';
        int y = 0;
        long long sumAll = n * m * (n * m + 1) / 2;
        long long l = 0;
        long long r = m;
        while (l < r - 1) {
            long long mid = (l + r) / 2;
            long long now_sum = mid * n * (mid + 1 + m * n - m) / 2;
            if (now_sum <= sumAll / 2) {
                l = mid;
            }
            else {
                r = mid;
            }
        }
        long long now_sum = l * n * (l + 1 + m * n - m) / 2;
        if (best > abs(now_sum - (sumAll - now_sum))) {
            best = abs(now_sum - (sumAll - now_sum));
            x = 'V';
            y = l;
        }
        now_sum = (l + 1) * n * (l + 2 + m * n - m) / 2;
        if (best > abs(now_sum - (sumAll - now_sum))) {
            best = abs(now_sum - (sumAll - now_sum));
            x = 'V';
            y = l + 1;
        }
        l = 0;
        r = n;
        while (l < r - 1) {
            long long mid = (l + r) / 2;
            now_sum = (m * m * mid * mid + m * mid) / 2;
            if (now_sum <= sumAll / 2) {
                l = mid;
            }
            else {
                r = mid;
            }
        }
        now_sum = (m * m * l * l + m * l) / 2;
        if (best > abs(now_sum - (sumAll - now_sum))) {
            best = abs(now_sum - (sumAll - now_sum));
            x = 'H';
            y = l;
        }
        now_sum = (m * m * (l + 1) * (l + 1) + m * (l + 1)) / 2;
        if (best > abs(now_sum - (sumAll - now_sum))) {
            best = abs(now_sum - (sumAll - now_sum));
            x = 'H';
            y = l + 1;
        }
        cout << x << " " << y + 1 << "\n";
    }
}