import random


def find_longest_anagram_subarray(a, b, n, m):
    letters = set(a).union(b)
    hash_letters = {q: random.randint(1, 10 ** 9 + 1) for q in letters}

    pref_a = [0] * n
    s_a = 0
    for i in range(n):
        s_a += hash_letters[a[i]]
        pref_a[i] = s_a

    pref_b = [0] * m
    s_b = 0
    for i in range(m):
        s_b += hash_letters[b[i]]
        pref_b[i] = s_b

    ans = 0
    for l in range(min(n, m), 0, -1):
        for i in range(0, n - l + 1):
            sub_a = pref_a[i + l - 1] - pref_a[i - 1] if i > 0 else pref_a[i + l - 1]
            for j in range(0, m - l + 1):
                sub_b = pref_b[j + l - 1] - pref_b[j - 1] if j > 0 else pref_b[j + l - 1]
                if sub_a == sub_b:
                    ans = l
                    break

            if ans:
                break

        if ans:
            break

    return ans


# Ввод данных и вывод результата
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    print(find_longest_anagram_subarray(a, b, n, m))