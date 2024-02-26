def merge_list(a, b):
    global count
    result = []
    n = len(a)
    m = len(b)
    first = 0
    second = 0
    while first < n and second < m:
        if a[first] <= b[second]:
            result.append(a[first])
            first += 1

        else:
            result.append(b[second])
            second += 1
            count += n - first

    result += a[first:] + b[second:]
    return result


def split_and_merge_list(a):
    n1 = len(a) // 2
    a1 = a[:n1]
    a2 = a[n1:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)


n = int(input())
a = list(map(int, input().split()))
count = 0

result = split_and_merge_list(a)
print(count)
print(*result)
