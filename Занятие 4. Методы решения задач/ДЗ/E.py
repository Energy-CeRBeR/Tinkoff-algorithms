def is_answer(m):
    s = 0
    count = 0
    for i in range(n):
        if a[i] + s <= m:
            s += a[i]
        else:
            count += 1
            s = a[i]
            if s > m:
                return False

    count += 1
    if count <= k:
        return True
    return False


n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 1
right = sum(a)
while right - left > 1:
    middle = (right + left) // 2
    if is_answer(middle):
        right = middle
    else:
        left = middle
print(right)
