import random
from G import find_longest_anagram_subarray as solver_optimized
from GG import find_longest_anagram_subarray as solver_garanted

k = 0
while True:
    k += 1
    n = random.randint(1, 100)
    m = random.randint(1, 100)
    a, b = [random.randint(1, 100000) for _ in range(n)], [random.randint(1, 100000) for _ in range(m)]

    res1, res2 = solver_garanted(a, b), solver_optimized(a, b, n, m)
    print(k)
    if res1 != res2:
        print(k)
        print(n, m)
        print(a)
        print(b)
        print(res1, res2)
        break


'''print(n)
print(*a)
print(m)
print(*b)'''