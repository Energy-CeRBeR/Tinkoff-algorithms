n = int(input())
a = []
for _ in range(n):
    t = list(map(int, input().split()))
    t1 = 3600 * t[0] + 60 * t[1] + t[2]
    t2 = 3600 * t[3] + 60 * t[4] + t[5]
    if t1 < t2:
        a.append([t1, t2])
    elif t1 > t2:
        a.append([t1, 86400])
        a.append([0, t2])

a.sort()
start_line = a[0][0]
end_line = a[0][1]
for i in range(1, len(a)):
    if a[i][0] > start_line:
        start_line = a[i][0]
    if a[i][1] < end_line:
        end_line = a[i][1]

print(start_line - end_line)