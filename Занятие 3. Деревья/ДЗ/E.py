def heapify(arr, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)


def heap_sort(arr):
    size = len(arr)

    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


n = int(input())
a = list(map(int, input().split()))

heap_sort(a)
print(*a, sep=" ")
