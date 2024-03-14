def find_min_greater_equal(arr, value, mn_arr, mx_arr):
    left = mn_arr
    right = mx_arr
    if right < value:
        return -1
    while right - left > 1:
        md = (left + right) // 2
        if md < value:
            left = md
        else:
            right = md
    return right



n = int(input())
d = set()
flag = -2
mn = 10 ** 28
mx = -10 ** 28
for _ in range(n):
    query = input().split()
    if query[0] == "+":
        if flag == -2:
            value = int(query[1])
        else:
            value = (flag + int(query[1])) % (10 ** 9)
        if value not in d:
            d.add(value)
            flag = -2
            mx = max(mx, value)
            mn = min(mn, value)

    elif query[0] == "?":
        value = int(query[1])
        result = find_min_greater_equal(list(d) )
        flag = result
        print(result)