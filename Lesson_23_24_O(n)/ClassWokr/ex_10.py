# Напишіть функцію, яка знаходить перетин двох списків. Порівняйте складність реалізації через:
# • два вкладених цикли - O(n²);
# • використання множин - O(n).
def intersection_loops(list1, list2):
    result = []
    for x in list1:
        for y in list2:
            if x == y and x not in result:
                result.append(x)
    return result


def intersection_sets(list1, list2):
    return list(set(list1) & set(list2))


import time

list1 = list(range(1000))
list2 = list(range(500, 1500))

start = time.time()
result1 = intersection_loops(list1, list2)
print(f"Час виконання з циклами: {time.time() - start}")

start = time.time()
result2 = intersection_sets(list1, list2)
print(f"Час виконання з множинами: {time.time() - start}")
