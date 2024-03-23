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


PRIME = 31
MOD = 10 ** 9 + 7

S = input()
m = int(input())

power = prime_power(len(S))
hash_S = hash_func(S)
for _ in range(m):
    a, b, c, d = map(int, input().split())
    if get_hash(hash_S, a, b) == get_hash(hash_S, c, d):
        print("Yes")
    else:
        print("No")
