#include <iostream>
#include <vector>
using namespace std;
int n, m, a[20];
long long s;
vector<int> cur, res;
void f(int pos = 0, long long sum = 0) {
    if (pos == m) {
        if (sum == n) {
            if (!res.size() || cur.size() < res.size()) {
                res = cur;
            }
            return;
        }
        return;
    }
    f(pos + 1, sum);
    cur.push_back(a[pos]);
    f(pos + 1, sum + a[pos]);
    cur.push_back(a[pos]);
    f(pos + 1, sum + a[pos] * 2);
    cur.pop_back();
    cur.pop_back();
}
int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a[i];
        s += a[i] * 2;
    }
    if (s < n) {
        cout << -1 << "\n";
        return 0;
    }
    f();
    if (!res.size()) {
        cout << 0 << "\n";
        return 0;
    }
    cout << res.size() << "\n";
    for (auto ans : res) cout << ans << " ";
    return 0;
}