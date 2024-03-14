def solve(x):
    if x == 1 or x == n ** 2:
        return int(x ** 0.5)
    return 1 + (x - 1) // 2 + (x - 1) % 2


n, k = map(int, input().split())
a = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
for q in a:
    print(*q, sep="\t")





