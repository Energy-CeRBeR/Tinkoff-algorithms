def alg(s):
    s = "".join(sorted(s))
    sorted_letters = "".join(sorted(set(s)))
    set_s = set(s)
    flag = True
    mn = "a"
    for q in set_s:
        count = s.count(q)
        if count != 1:
            flag = False
        if count % 2 != 0:
            mn = min(mn, q)

    if flag:
        return min(set_s)

    arr = []
    for q in sorted_letters:
        count = s.count(q)
        count -= count % 2
        arr.extend([q] * count)

    n = len(arr) + (mn != "a")
    arr.sort()
    ans = [None] * n
    i = 0
    while len(arr) > 0:
        ans[i] = arr.pop(0)
        ans[n - i - 1] = arr.pop(0)
        i += 1
    if mn != "a":
        ans[n // 2] = mn
    ans = "".join(ans)
    return ans


n = int(input())
line = input()
ans = alg(line)
print(ans)

