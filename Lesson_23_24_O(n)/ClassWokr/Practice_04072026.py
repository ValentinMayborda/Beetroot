"""
Напишіть функцію, яка знаходить перетин двох списків.

 Порівняйте складність реалізації через:
• два вкладених цикли - O(n²);
• використання множин - O(n).
"""
import time

lst1 = list(range(1000))
lst2 = list(range(500, 1500))

# два вкладених цикли - O(n²)
def intersection_loop(ls1, ls2):

    rezult = []
    for i in ls1:
        for j in ls2:
            if i == j and i not in rezult:
                rezult.append(i)

    return rezult

# використання множин - O(n).
def intersection_sets(ls1, ls2):
    return list(set(ls1) & set(ls2))


start = time.time()
rezult1 = intersection_loop(lst1, lst2)
print(f'Час виконання циклу О(n^2) - {time.time() -start}')

start = time.time()
rezult2 = intersection_sets(lst1, lst2)
print(f'Час виконання  O(n) - {time.time() -start}')
