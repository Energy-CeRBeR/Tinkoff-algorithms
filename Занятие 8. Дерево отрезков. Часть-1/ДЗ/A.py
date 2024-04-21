def build_tree(v, lv, rv):
    if rv - lv == 1:
        tree[v] = a[lv]
    else:
        md = (lv + rv) // 2
        build_tree(2 * v + 1, lv, md)
        build_tree(2 * v + 2, md, rv)
        tree[v] = tree[2 * v + 1] + tree[2 * v + 2]


def modify(v, lv, rv, ind, x):
    if rv - lv == 1:
        tree[v] = x
    else:
        md = (lv + rv) // 2
        if ind < md:
            modify(2 * v + 1, lv, md, ind, x)
        else:
            modify(2 * v + 2, md, rv, ind, x)
        tree[v] = tree[2 * v + 1] + tree[2 * v + 2]


def get_sum(v, lv, rv, l, r):
    if l >= rv or r <= lv:
        return 0
    if lv >= l and rv <= r:
        return tree[v]
    md = (lv + rv) // 2
    s1 = get_sum(2 * v + 1, lv, md, l, r)
    s2 = get_sum(2 * v + 2, md, rv, l, r)
    return s1 + s2


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

size = 1
while size < n:
    size *= 2
a = a + [0] * (size - n)

tree = [0] * (2 * size - 1)
build_tree(0, 0, size)
for _ in range(m):
    command = tuple(map(int, input().split()))
    if command[0] == 1:
        modify(0, 0, size, command[1], command[2])
    else:
        s = get_sum(0, 0, size, command[1], command[2])
        print(s)
