#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <cmath>
#define LL long long
#define INF 0x3f3f3f3f
#define mod 1000000007
using namespace std;
const int maxn = 500000 + 5;
struct Point{
    LL x,y,z;
    int op;
    Point(){}
    Point(LL xx, LL yy):x(xx),y(yy){}
    Point(LL xx, LL yy, LL zz, int oo):x(xx),y(yy),z(zz),op(oo){}
    bool operator < (const Point & p) const{
        if(x == p.x) return op < p.op;
        return x < p.x;
    }
}pt[maxn*4];
struct Line{
    Point s,e;
    Line(){}
    Line(Point ss, Point ee):s(ss),e(ee){}
}shu[maxn],heng[maxn];
bool cmp1(Line a, Line b){
    if(a.s.y == b.s.y) return a.s.x < b.s.x;
    return a.s.y < b.s.y;
}
bool cmp2(Line a, Line b){
    if(a.s.x == b.s.x) return a.s.y < b.s.y;
    return a.s.x < b.s.x;
}
LL id[maxn*4];
LL sum[maxn*4];
LL lowbit(LL x){
    return x & (-x);
}
void add(LL x, LL c){
    while(x < maxn*4){
        sum[x] += c;
        x += lowbit(x);
    }
}
LL getsum(int x){
    LL ans = 0;
    while(x > 0){
        ans += sum[x];
        x -= lowbit(x);
    }
    return ans;
}
map<LL, int> maps;
int main(){
    int n;
    scanf("%d",&n);
    LL ans = 0;
    int idx = 0;
    int cnt = 0;
    int na = 0, nb = 0, naa = 0, nbb = 0;
    for(int i=0; i<n; i++){
        LL x1,y1,x2,y2;
        scanf("%lld%lld%lld%lld",&x1,&y1,&x2,&y2);
        if(x1 == x2){
            if(y1 > y2) swap(y1,y2);
            shu[na++] = Line(Point(x1,y1),Point(x2,y2));
        }
        else{
            if(x1 > x2) swap(x1,x2);
            heng[nb++] = Line(Point(x1,y1),Point(x2,y2));
        }
    }
    sort(shu,shu+na,cmp2);
    sort(heng,heng+nb,cmp1);
    for(int i=1; i<na; i++){
        if(shu[i].s.x != shu[i-1].s.x || (shu[i].s.x == shu[i-1].s.x && shu[i-1].e.y < shu[i].s.y)){
            shu[naa++] = shu[i-1];
        }
        else{
            shu[i].s.y = min(shu[i].s.y,shu[i-1].s.y);
            shu[i].e.y = max(shu[i].e.y,shu[i-1].e.y);
        }
    }
    if(na > 0)
    shu[naa++] = shu[na-1];
    for(int i=1; i<nb; i++){
        if(heng[i].s.y != heng[i-1].s.y || (heng[i].s.y == heng[i-1].s.y && heng[i-1].e.x < heng[i].s.x)){
            heng[nbb++] = heng[i-1];
        }
        else{
            heng[i].s.x = min(heng[i].s.x,heng[i-1].s.x);
            heng[i].e.x = max(heng[i].e.x,heng[i-1].e.x);
        }
    }
    if(nb > 0)
    heng[nbb++] = heng[nb-1];
    for(int i=0; i<naa; i++){
        LL x1,y1,x2,y2;
        x1 = shu[i].s.x, y1 = shu[i].s.y , x2 = shu[i].e.x, y2 = shu[i].e.y;
        pt[cnt++] = Point(x1,y1,y2,1);
        id[idx++] = y1;
        id[idx++] = y2;
        ans += y2-y1+1;
    }
    for(int i=0; i<nbb; i++){
        LL x1,y1,x2,y2;
        x1 = heng[i].s.x, y1 = heng[i].s.y , x2 = heng[i].e.x, y2 = heng[i].e.y;
        pt[cnt++] = Point(x1,y1,1,0);
        pt[cnt++] = Point(x2+1,y2,-1,0);
        id[idx++] = y1;
        ans += x2-x1+1;
    }
    LL tot = 0;
    sort(id,id+idx);
    idx = unique(id,id+idx)-id;
    for(int i=0; i<idx; i++){
        maps[id[i]] = i+1;
    }
    sort(pt,pt+cnt);
    for(int i=0; i<cnt; i++){
        if(pt[i].op == 0){
            add(maps[pt[i].y],pt[i].z);
        }
        else{
            tot += getsum(maps[pt[i].z]) - getsum(maps[pt[i].y]-1);
        }
    }
    printf("%lld\n",ans-tot);
}