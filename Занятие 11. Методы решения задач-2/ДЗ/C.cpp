#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string** dp;
int main() {
    string s1, s2;
    long long i, j;
    cin >> s1;
    s2 = s1;
    long long m = s1.size() + 1;
    reverse(s2.begin(), s2.end());
    dp = new string * [m];
    for (i = 0; i < m; i++)dp[i] = new string[m];
    for (i = 1; i < m; i++) {
        for (j = 1; j < m; j++) {
            if (s1[i - 1] == s2[j - 1])dp[i][j] = dp[i - 1][j - 1] + s2[j - 1];
            else {
                if (dp[i - 1][j].size() > dp[i][j - 1].size())dp[i][j] = dp[i - 1][j];
                else dp[i][j] = dp[i][j - 1];
            }
        }
    }
    cout << dp[m - 1][m - 1].size() << endl;
    cout << dp[m - 1][m - 1];
    return 0;
}