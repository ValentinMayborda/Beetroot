def selection_sort(arr):
   n = len(arr)
   for i in range(n):
       min_idx = i                       # припускаємо, що поточний — мінімум
       for j in range(i + 1, n):         # шукаємо справжній мінімум
           if arr[j] < arr[min_idx]:
               min_idx = j
       arr[i], arr[min_idx] = arr[min_idx], arr[i]   # ставимо мінімум на місце
   return arr

print(selection_sort([5, 3, 8, 1, 4]))
