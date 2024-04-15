def damerau_levenshtein_distance(s1, s2):
    d = {}
    l_1 = len(s1)
    l_2 = len(s2)
    for i in range(-1, l_1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, l_2 + 1):
        d[(-1, j)] = j + 1

    for i in range(l_1):
        for j in range(l_2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,
                d[(i, j - 1)] + 1,
                d[(i - 1, j - 1)] + cost,
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)

    return d[l_1 - 1, l_2 - 1]


a = input()
b = input()
length = damerau_levenshtein_distance(a, b)
print(length)
