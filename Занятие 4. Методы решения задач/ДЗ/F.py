n = int(input())
a = []
for _ in range(n):
    line = list(map(int, input().split()))
    a.append(line)
a.sort()

length = a[0][1] - a[0][0]
end_line = a[0][1]
for i in range(1, n):
    length += max(a[i][1], end_line) - max(a[i][0], end_line)
    end_line = max(end_line, a[i][1])

print(length)
