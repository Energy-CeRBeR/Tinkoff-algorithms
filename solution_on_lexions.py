def find_substring_indices(p, t):
    indices = []
    for i in range(len(t) - len(p) + 1):
        mismatch_count = 0
        for j in range(len(p)):
            if p[j] != t[i + j]:
                mismatch_count += 1
                if mismatch_count > 1:
                    break
        if mismatch_count <= 1:
            indices.append(i + 1)
    return indices


p = input()
t = input()

result = find_substring_indices(p, t)
print(result)
