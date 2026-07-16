def merge(arr, left, mid, right):
    temp = []

    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]


def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    merge(arr, left, mid, right)


numbers = [38, 27, 43, 3, 9, 82, 10]
merge_sort(numbers, 0, len(numbers) - 1)
print(numbers)
