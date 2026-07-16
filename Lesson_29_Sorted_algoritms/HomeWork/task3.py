import random


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high, limit):
    if high - low + 1 <= limit:
        insertion_sort(arr, low, high)
        return

    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1, limit)
        quick_sort(arr, pi + 1, high, limit)


numbers = [random.randint(1, 100) for _ in range(20)]

print("До:", numbers)

quick_sort(numbers, 0, len(numbers) - 1, limit=10)

print("Після:", numbers)
