# O(n) - Лінійна складність
def find_max(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]
print(find_max(arr))