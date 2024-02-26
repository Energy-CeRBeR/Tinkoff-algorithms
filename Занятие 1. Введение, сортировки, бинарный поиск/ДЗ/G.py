n = int(input())
a = [int(i) for i in range(1, n + 1)]

for i in range(2, n):
    a[i], a[i // 2] = a[i // 2], a[i]

print(*a)