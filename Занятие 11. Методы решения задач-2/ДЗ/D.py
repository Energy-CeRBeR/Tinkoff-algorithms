import math
l, n = map(int, input().split())
d = []
a = list(map(int, input().split()))
a.insert(0, 0)
a.append(l)
n += 2
for i in range(n):
    d.append([0] * n)
for j in range(1, n):
    for i in range(j - 2, -1, -1):
        d[i][j] = math.inf
        for k in range(i + 1, j):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        d[i][j] += a[j] - a[i]
print(d[0][n - 1])