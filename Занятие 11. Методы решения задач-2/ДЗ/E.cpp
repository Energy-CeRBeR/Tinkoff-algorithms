#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;
const int MAX_LEN = 1e9;
int n;
string str;
vector<vector<int> > mas;
void input()
{
    cin >> str;
    n = str.size();
    mas = vector<vector<int> >(n, vector<int>(n, 0));
}
int count(int num)
{
    int amount = 0;
    while (num) {
        num /= 10;
        amount++;
    }
    return amount;
}
string getAnswer(int i, int j) {

    if (i == j)
        return string(&str[i], 1);
    int res = MAX_LEN;
    int LEN = j - i + 1;
    for (int step = 1; step <= LEN / 2; step++)
    {
        if (LEN % step != 0) continue;
        bool isOK = true;
        for (int cur = 0; cur < step; cur++) {
            for (int pos = i + cur; pos <= j; pos += step) {
                if (str[i + cur] != str[pos]) {
                    isOK = false;
                    break;
                }
            }
        }
        if (isOK) {
            int curLen = count((j - i + 1) / step) + 2 + mas[i][i + step - 1];
            if (curLen == mas[i][j]) {

                char buf[10];
                sprintf(buf, "%d", (j - i + 1) / step);
                return string(buf) + "(" + getAnswer(i, i + step - 1) + ")";
            }

        }
    }

    for (int m = i; m < j; m++)
        if (mas[i][m] + mas[m + 1][j] == mas[i][j])
            return getAnswer(i, m) + getAnswer(m + 1, j);
}
void solve()
{
    for (int len = 0; len < n; len++) {
        for (int i = 0; i < n; i++) {
            int j = i + len;
            if (j >= n) break;

            if (len == 0) mas[i][j] = 1;

            else {
                int res = MAX_LEN;
                int LEN = j - i + 1;
                for (int step = 1; step <= LEN / 2; step++)
                {
                    if (LEN % step != 0) continue;
                    bool isOK = true;
                    for (int cur = 0; cur < step; cur++) {
                        for (int pos = i + cur; pos <= j; pos += step) {
                            if (str[i + cur] != str[pos]) {
                                isOK = false;
                                break;
                            }
                        }
                    }
                    if (isOK) {
                        int curLen = count(LEN / step) + 2 + mas[i][i + step - 1];
                        res = min(res, curLen);
                    }
                }

                for (int m = i; m < j; m++)
                    res = min(res, mas[i][m] + mas[m + 1][j]);

                mas[i][j] = res;
            }
        }
    }

    string ans = getAnswer(0, n - 1);
    cout << ans;
}
int main()
{

    input();
    solve();
    return 0;
}