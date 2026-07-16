def selection_sort(lst):
    n = len(lst)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


l = [5, 3, 8, 1, 4]

print(selection_sort(l))
