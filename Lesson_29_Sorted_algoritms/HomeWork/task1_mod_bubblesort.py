def mod_bubblesort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        #Йдемо зліва направо
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # перевірка чи масив вже відсортований
        if not swapped:
            break

        swapped = False
        end -= 1

        # Йдемо справа наліво
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        start +=1

    return arr

print(mod_bubblesort([5, 3, 8, 1, 4, 10, 4, 3, 15]))