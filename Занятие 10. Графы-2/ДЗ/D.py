import sys

input = sys.stdin.readline


def sol(n, a, d):
    a.append(0)
    if n == 1: return 0
    left = [i - 1 for i in range(n)]
    right = [i + 1 for i in range(n)]
    att = [0] * n
    die = []
    if d[0] < a[1]: die.append(0)
    att[0] = a[1]
    for i in range(1, n - 1):
        att[i] = a[i - 1] + a[i + 1]
        if d[i] < a[i - 1] + a[i + 1]:
            die.append(i)
    if d[n - 1] < a[n - 2]: die.append(n - 1)
    att[n - 1] = a[n - 2]

    res = [str(len(die))]
    dead = set(die)
    for i in range(n - 1):
        n_die = []
        change = set()
        for j in die:
            if left[j] >= 0:
                right[left[j]] = right[j]
                change.add(left[j])
            if right[j] < n:
                left[right[j]] = left[j]
                change.add(right[j])
            if 0 <= left[j] < n:
                att[left[j]] += a[right[j]] - a[j]
            if 0 <= right[j] < n:
                att[right[j]] += a[left[j]] - a[j]

        for j in change:
            if att[j] > d[j] and j not in dead:
                n_die.append(j)
                dead.add(j)
        die = n_die
        res.append(str(len(die)))
    return ' '.join(res)



n = int(input())
a = list(map(int, input().split()))
d = list(map(int, input().split()))
print(sol(n, a, d))
