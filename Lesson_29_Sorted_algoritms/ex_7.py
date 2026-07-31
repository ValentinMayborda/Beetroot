def insertion_sort(arr):
   for i in range(1, len(arr)):
       key = arr[i]     # елемент, який вставляємо
       j = i - 1
       # зсуваємо елементи вправо, поки вони більші за key
       while j >= 0 and arr[j] > key:
           arr[j + 1] = arr[j]
           j -= 1
       arr[j + 1] = key   # вставляємо на правильну позицію
   return arr

print(insertion_sort([5, 3, 8, 1, 4]))

