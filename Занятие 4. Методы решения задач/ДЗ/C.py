def is_answer(distance):
    count = 1
    last_p = p[0]
    for i in range(1, n):
        if last_p + distance <= p[i]:
            count += 1
            last_p = p[i]
        if count == k:
            return True

    return False


n, k = map(int, input().split())
p = list(map(int, input().split()))

left = 0
right = 10 ** 9
while right - left > 1:
    m = (left + right) // 2
    if is_answer(m):
        left = m
    else:
        right = m

print(left)
