import random
import string


def cyclic_shifts(s):
    n = len(s)
    end_s = s
    mn_s = s
    for i in range(1, n):
        shift = end_s[-1] + end_s[:-1]
        end_s = shift
        mn_s = min(mn_s, end_s)
    return mn_s


s = "".join(random.choice(string.ascii_lowercase) for _ in range(10 ** 5))
print(cyclic_shifts(s))
