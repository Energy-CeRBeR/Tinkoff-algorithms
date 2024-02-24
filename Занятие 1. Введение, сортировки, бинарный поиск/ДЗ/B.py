def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    mid = (left + right) // 2
    mn_elem = min(arr[left], arr[right])
    mn_dif = 10 ** 28

    if abs(x - arr[left]) < mn_dif:
        mn_dif = abs(x - arr[left])
        mn_elem = arr[left]
    elif abs(x - arr[left]) == mn_dif:
        mn_elem = min(mn_elem, arr[left])

    if abs(x - arr[right]) < mn_dif:
        mn_dif = abs(x - arr[right])
        mn_elem = arr[right]
    elif abs(x - arr[right]) == mn_dif:
        mn_elem = min(mn_elem, arr[right])

    while right - left >= 0:
        if arr[mid] == x:
            return arr[mid]

        elif arr[mid] < x:
            left = mid + 1
            if abs(x - arr[mid]) < mn_dif:
                mn_dif = abs(x - arr[mid])
                mn_elem = arr[mid]
            elif abs(x - arr[mid]) == mn_dif:
                mn_elem = min(mn_elem, arr[mid])

        else:
            right = mid - 1
            if abs(x - arr[mid]) < mn_dif:
                mn_dif = abs(x - arr[mid])
                mn_elem = arr[mid]
            elif abs(x - arr[mid]) == mn_dif:
                mn_elem = min(mn_elem, arr[mid])

        mid = (left + right) // 2

    return mn_elem


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for num in b:
    print(binary_search(a, num))