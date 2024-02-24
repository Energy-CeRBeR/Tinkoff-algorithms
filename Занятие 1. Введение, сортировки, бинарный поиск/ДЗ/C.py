import sys


def bin_search(n):
    left = 1
    right = n
    while right - left >= 0:
        mid = (left + right) // 2
        mid = min(mid, n)
        answer = query(mid)

        if answer == "<":
            right = mid - 1
        else:
            left = mid + 1

    if left <= n and query(left) == "<":
        mid = left - 1

    print(f"! {mid}")


def query(x):
    print(x)
    sys.stdout.flush()
    return input()


n = int(input())
bin_search(n)