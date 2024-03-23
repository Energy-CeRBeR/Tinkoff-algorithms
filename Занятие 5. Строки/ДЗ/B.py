def z_func(s):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
            if i + z[i] > right:
                left, right = i, i + z[i]
    return z


def find_pattern(pattern, text):
    s = pattern + "#" + text
    z = z_func(s)
    return [i - len(pattern) - 1 for i in range(len(z)) if z[i] == len(pattern)]


T = input()
q = int(input())
for _ in range(q):
    s_i = input()
    ans_i = find_pattern(s_i, T)
    print(len(ans_i), end=" ")
    print(*ans_i)
