def L(k):
    return ((n - 1) * m * n + (k + 1) * n) * k / 2


def R(k):
    return ((n - 1) * m * n + (k + 1 + m) * n) * (m - k) / 2


def U(k):
    return (k * m ** 2 + m) * k / 2


def D(k):
    return ((k + n) * m ** 2 + m) * (n - k) / 2


def binary_search_V():
    left = 0
    right = m
    middle = (left + right) // 2
    result = [abs(L(middle) - R(middle)), 0]
    while left < right:
        #print(middle)
        l = L(middle)
        r = R(middle)
        if l <= r and R(middle + 1) < L(middle + 1):
            #print(L(middle + 1), R(middle + 1))
            if abs(L(middle + 1) - R(middle + 1)) < abs(r - l):
                middle += 1
            #print(middle, "middle LR")
            return tuple([abs(R(middle) - L(middle)), middle])

        elif l < r:
            left = middle + 1
        else:
            right = middle - 1
    
        if abs(L(middle) - R(middle)) < result[0]:
            result[0] = abs(L(middle) - R(middle))
            result[1] = middle
            
        middle = (left + right) // 2

    return tuple(result)


def binary_search_H():
    left = 0
    right = m
    middle = (left + right) // 2
    result = [abs(U(middle) - D(middle)), 0]
    while left < right:
        #print(middle)
        u = U(middle)
        d = D(middle)
        #print(u, d, middle, "UD")
        if u == d:
            return middle

        if u < d and D(middle + 1) < U(middle + 1):
            if abs(U(middle + 1) - D(middle + 1)) < abs(d - u):
                middle += 1
            return tuple([abs(U(middle) - D(middle)), middle])

        elif u < d:
            left = middle + 1
        else:
            right = middle - 1
        
        if abs(U(middle) - D(middle)) < result[0]:
            result[0] = abs(U(middle) - D(middle))
            result[1] = middle
            
        middle = (left + right) // 2

    return tuple(result)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    res1 = binary_search_V()
    res2 = binary_search_H()
    if res1[0] < res2[0]:
        print("V", res1[1] + 1)
    else:
        print("H", res2[1] + 1)

    
