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


def get_hash_a(hashes, l, r):
    return (hashes[r] - hashes[l - 1] * power_a[r - l + 1]) % MOD


def get_hash_b(hashes, l, r):
    return (hashes[r] - hashes[l - 1] * power_b[r - l + 1]) % MOD


def cyclic_shifts(s):
    n = len(s)
    result = dict()
    for i in range(1, n + 1):
        shift = get_hash_b(hash_b, i, i + n - 1)
        result[shift] = ""
    return result


def solve(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    count = 0
    for i in range(1, n1 - n2 + 2):
        substr_h = get_hash_a(hash_a, i, i + n2 - 1)
        if substr_h in c:
            count += 1

    return count


PRIME = 31
MOD = 10 ** 9 + 7

a = input()
b = input()
hash_a = hash_func(2 * a)
hash_b = hash_func(2 * b)
power_a = prime_power(len(2 * a))
power_b = prime_power(len(2 * b))

c = cyclic_shifts(b)
print(solve(a, b))
