# O(2^n) - Експонеційна складність
from pip._internal import operations


def generate_sudsets(arr):
    subsets = [[]]
    for num in arr:
        new_subsets = [subset + [num] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets

arr = [1, 2, 3]
print(generate_sudsets(arr))  #O(2^n)
# n = 10
# # 1024 operations
# n = 20 ?