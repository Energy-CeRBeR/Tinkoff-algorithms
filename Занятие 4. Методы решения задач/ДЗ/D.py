def get_count(md):
    count = 0
    for i in range(1, n + 1):
        count += min(md // i, n)
    return count


n, k = map(int, input().split())

left = 1
right = n * n
while left < right:
    middle = (left + right) // 2
    if get_count(middle) < k:
        left = middle + 1
    else:
        right = middle

print(left)
