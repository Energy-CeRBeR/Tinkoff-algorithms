t = int(input())
INF = 10 ** 40

for i in range(1, t + 1):
    sx, sy = map(int, input().split())
    ans = INF
    ansS = ""
    n = sx * sy
    total = n * (n + 1)
    total1 = (1 + (n - sy + 1)) * sx

    cl, cr = 0, sy
    cla, cra = 0, total
    while cr - cl > 1:
        mid = (cl + cr) >> 1
        s1 = (total1 + sx * (mid - 1)) * mid
        if s1 > total - s1:
            cr = mid
            cra = s1
        else:
            cl = mid
            cla = s1
    if abs(cla - (total - cla)) < ans:
        ans = abs(cla - (total - cla))
        ansS = "V " + str(cl + 1)
    if abs(cra - (total - cra)) < ans:
        ans = abs(cra - (total - cra))
        ansS = "V " + str(cr + 1)

    cl, cr = 0, sx
    cla, cra = 0, total
    while cr - cl > 1:
        mid = (cl + cr) >> 1
        cnt = mid * sy
        s1 = cnt * (cnt + 1)
        if s1 > total - s1:
            cr = mid
            cra = s1
        else:
            cl = mid
            cla = s1
    if abs(cla - (total - cla)) < ans:
        ans = abs(cla - (total - cla))
        ansS = "H " + str(cl + 1)
    if abs(cra - (total - cra)) < ans:
        ans = abs(cra - (total - cra))
        ansS = "H " + str(cr + 1)

    print(ansS)
