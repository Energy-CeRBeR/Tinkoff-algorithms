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
typedef long long LL; typedef long long ll; typedef unsigned long long uLL; typedef unsigned long long ull; typedef unsigned int uint; typedef unsigned char uchar; typedef long double ld; typedef long double Ld;


struct Segment {
    int y, x1, x2, SegmentNum;
    bool type;

    Segment(int _y = 0, int _x1 = 0, int _x2 = 0, int _SegmentNum = 0, bool _type = false) {
        y = _y;
        x1 = _x1;
        x2 = _x2;
        SegmentNum = _SegmentNum;
        type = _type;
    }
};
bool cmp(Segment a, Segment b) { return (a.y == b.y && !a.type && b.type) || a.y < b.y; }


struct Node {
    int maxx, pos, mem;

    Node(int _maxx = 0, int _pos = -1, int _mem = 0) {
        maxx = _maxx;
        pos = _pos;
        mem = _mem;
    }

    Node operator + (Node other) {
        Node res(
            max(maxx, other.maxx),
            (maxx > other.maxx ? pos : other.pos)
        );
        return res;
    }
};


int SIZE = 1;

void push(vector<Node>& tree, int v) {
    tree[v].maxx += tree[v].mem;
    if (v < SIZE) {
        tree[v * 2].mem += tree[v].mem;
        tree[v * 2 + 1].mem += tree[v].mem;
    }
    tree[v].mem = 0;
}

void addTree(vector<Node>& tree, int v, int l, int r, int a, int b, bool c) {
    push(tree, v);

    if (a > r || l > b) return;

    if (a <= l && r <= b) {
        tree[v].mem += (c ? -1 : 1);
        push(tree, v);
        return;
    }

    int m = (l + r) / 2;
    addTree(tree, v * 2, l, m, a, b, c);
    addTree(tree, v * 2 + 1, m + 1, r, a, b, c);
    tree[v] = tree[v * 2] + tree[v * 2 + 1];
}

signed main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    const int MAX_SIZE = 4e5, ADDITIONAL = 2e5;

    while (SIZE <= MAX_SIZE) SIZE <<= 1;

    vector<Node> tree(4 * MAX_SIZE);
    for (int i = SIZE; i < tree.size(); ++i) {
        tree[i].pos = i - SIZE + 1;
        tree[i].maxx = 0;
    }
    for (int i = SIZE - 1; i >= 1; --i) tree[i] = tree[i * 2] + tree[i * 2 + 1];


    int n;
    cin >> n;

    vector<Segment> border(2 * 100000);
    int x1, y1, x2, y2;
    for (int i = 0; i < 2 * n; i += 2) {
        cin >> x1 >> y1 >> x2 >> y2;

        x1 += ADDITIONAL; y1 += ADDITIONAL;
        x2 += ADDITIONAL; y2 += ADDITIONAL;

        border[i] = Segment(y2, x1, x2, i, true);
        border[i + 1] = Segment(y1, x1, x2, i, false);
    }

    sort(border.begin(), border.begin() + 2 * n, cmp);

    int res = -1, resX = -1, resY = -1;
    for (int i = 0; i < 2 * n; ++i) {
        addTree(tree, 1, 1, SIZE, border[i].x1, border[i].x2, border[i].type);

        if (tree[1].maxx > res) {
            res = tree[1].maxx;
            resX = tree[1].pos - ADDITIONAL;
            resY = border[i].y - ADDITIONAL;
        }
    }

    cout << res << endl
        << resX << ' ' << resY << endl;

    return 0;
}