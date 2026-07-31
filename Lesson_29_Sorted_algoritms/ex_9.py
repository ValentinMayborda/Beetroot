# 1. Розбиття (знайти опорний елемент)
# 2. Перестановка елементів
# 3. Рекурсія: Повторюємо те саме для лівої і правої частини масиву
def quick_sort(arr):
    # print(f"Quick sort: {arr}")
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    print('PIVOT: ', pivot)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print('LEFT: ', left)
    print('MIDDLE: ', middle)
    print('RIGHT: ', right)
    print('======')

    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([5, 2, 6, 1, 9, 3, 8, 4, 7, 5, 2, 5]))
# O(n log n)
# O(n**2)
# sort
# TimSort -> InsertionSort + MergeSort