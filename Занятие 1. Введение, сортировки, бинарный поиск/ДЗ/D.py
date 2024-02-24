def search_root(c):
    left = -1
    right = 10 ** 5
    eps = 10e-10

    while right - left >= eps:
        x = (left + right) / 2

        if x ** 2 + (x + 1) ** 0.5 < c:
            left = x

        else:
            right = x

    return x


c = float(input())

ans = search_root(c)
print(ans)