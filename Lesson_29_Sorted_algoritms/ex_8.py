def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# arr = [5, 2, 6, 1, 9, 3, 8, 4, 7]
# print(merge_sort(arr))


orders_monday = [101, 205, 307, 412]
orders_tuesday = [103, 201, 305, 410]
all_orders = merge(orders_monday, orders_tuesday)
print(all_orders)

