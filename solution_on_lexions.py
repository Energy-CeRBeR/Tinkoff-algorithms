def sumseq(a1, step, n):
    return (2 * a1 + step * (n - 1)) * n // 2


def diffhorizontal(y):
    top = sumseq(1, 1, m * (y - 1))
    total = sumseq(1, 1, m * n)
    button = total - top
    return top - button


def diffvertical(x):
    left = n * sumseq(0, 1, x - 1) + (x - 1) * sumseq(1, m, n)
    total = sumseq(1, 1, m * n)
    right = total - left
    return left - right


def solve(n, m):
    (diffV, indexV) = binsearch(1, m, diffvertical)
    (diffH, indexH) = binsearch(1, n, diffhorizontal)
    if abs(diffH) < abs(diffV):
        print("H", str(int(indexH)))
    else:
        print("V", str(int(indexV)))


def binsearch(left, right, diff):
    if right - left <= 1:
        dleft = diff(left)
        dright = diff(right)
        if abs(dleft) < abs(dright):
            return dleft, left
        else:
            return dright, right
    mid = (left + right) // 2
    dmid = diff(mid)
    if dmid < 0:
        return binsearch(mid, right, diff)
    else:
        return binsearch(left, mid, diff)


t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    solve(n, m)
