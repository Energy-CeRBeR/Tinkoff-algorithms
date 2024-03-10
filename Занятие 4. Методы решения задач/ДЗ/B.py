n, m, k = map(int, input().split())
ps = [[0 for _ in range(m)] for _ in range(n)]
a = []
for i in range(n):
    line = list(map(int, input().split()))
    s = 0
    for j in range(m):
        s += line[j]
        ps[i][j] = s

for _ in range(k):
    y1, x1, y2, x2 = map(lambda x: int(x) - 1, input().split())
    s = 0
    for j in range(y1, y2 + 1):
        s += ps[j][x2] - ps[j][x1 - 1] if x1 != 0 else ps[j][x2]
    print(s)
