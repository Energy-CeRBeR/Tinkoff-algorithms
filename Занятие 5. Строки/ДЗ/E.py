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


def cyclic_shifts(s):
    n = len(s)
    end_s = s
    mn_s = s
    for i in range(1, n):
        shift = end_s[-1] + end_s[:-1]

        end_s = shift
    return mn_s


PRIME = 31
MOD = 10 ** 9 + 7

p = input()
t = input()

# power = prime_power(len(S))
