#include <algorithm>
#include <iostream>
#include <iterator>
#include <limits.h>
#include <cassert>
#include <cstring>
#include <float.h>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <math.h>
#include <random>
#include <vector>
#include <cmath>
#include <deque>
#include <queue>
#include <map>
#include <set>

using namespace std;
const int MOD = 1e9 + 7;


#define all(_x) (_x).begin(), (_x).end()
#define print_array(_v) for(int i=0;i<(_v).size();++i){cout<<(_v)[i]<<' ';}cout<<endl;


signed main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    a[0] = 0;
    a[n - 1] = 0;
    for (int i = 1; i < n - 1; ++i) cin >> a[i];

    vector<int> d(n, INT_MAX), p(n);
    d[0] = a[0];

    for (int i = 1; i < n; ++i) {
        int last_min = i - 1;
        for (int j = max(0, i - k); j < i; ++j) {
            if (d[last_min] < d[j]) {
                last_min = j;
            }
        }
        d[i] = d[last_min] + a[i];
        p[i] = last_min;
    }

    cout << d.back() << endl;
    int cur = n - 1;
    vector<int> ans = { cur + 1 };

    while (cur != 0) {
        cur = p[cur];
        ans.push_back(cur + 1);
    }
    reverse(all(ans));

    cout << ans.size() - 1 << endl;
    print_array(ans);
}