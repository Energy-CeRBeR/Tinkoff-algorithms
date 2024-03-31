def prime_power(n):
    pow = [1] * (n + 1)
    for i in range(1, n + 1):
        pow[i] = (pow[i - 1] * PRIME) % MOD
    return pow


def hash_func(s):
    hashes = [0] * (len(s) + 1)
    for i in range(len(s)):
        hashes[i + 1] = (hashes[i] * PRIME + (ord(s[i]) - ord('a') + 1)) % MOD
    return hashes


def get_hash(hashes, l, r):
    return (hashes[r] - hashes[l - 1] * power[r - l + 1]) % MOD


def solve(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 > n2:
        return 0, []

    indexes = list()
    count = 0
    end_s = s2[:n1]
    if end_s == s1:
        count += 1
        indexes.append(1)
    else:
        flag = True
        k = 0
        for j in range(n1):
            if end_s[j] != s1[j]:
                k += 1
                if k > 1:
                    flag = False
                    break
        if flag:
            count += 1
            indexes.append(1)

    for i in range(1, n2 - n1 + 1):
        end_s = end_s[1:] + s2[i + n1 - 1]
        if end_s == s1:
            count += 1
            indexes.append(i + 1)
        else:
            flag = True
            k = 0
            for j in range(n1):
                if end_s[j] != s1[j]:
                    k += 1
                    if k > 1:
                        flag = False
                        break
            if flag:
                count += 1
                indexes.append(i + 1)
    return count, indexes


# PRIME = 31
# MOD = 10 ** 9 + 7

p = input()
t = input()
# hash_t = hash_func(t)
# power = prime_power(len(t))

ans = solve(p, t)
print(ans[0])
print(*ans[1])
