def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # оптимізація: якщо обмінів не було — масив вже готовий
        for j in range(0, n - i - 1):  # n-i-1: останні i елементів вже на місці
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
        if not swapped:  # ранній вихід, якщо масив вже відсортований
            break
    return arr

print(bubble_sort([5, 3, 8, 1, 4]))  # [1, 3, 4, 5, 8]
