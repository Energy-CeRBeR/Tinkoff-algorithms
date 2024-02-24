def binary_search(arr, elem, left=None, right=None):
    if left is None or right is None:
        left = 0
        right = len(a) - 1

    while right - left >= 0:
        m = (left + right) // 2

        if arr[m] == elem:
            return "YES"
        elif arr[m] < elem:
            left = m + 1
        else:
            right = m - 1

    return "NO"


n, k = map(int, input().split())
a = list(map(int, input().split()))
requests = list(map(int, input().split()))

for num in requests:
    print(binary_search(a, num))