"""Напишіть функцію з назвою choose_func, яка приймає:

список чисел (nums);
дві callback-функції (func1 і func2).

Якщо всі числа в списку є додатними, виконайте першу функцію над цим списком і поверніть її результат.
В іншому випадку поверніть результат виконання другої функції."""

def choose_func(nums: list, func1, func2):

    flag = True
    for num in nums:
        if num < 0:
            flag = False

    if flag:
        return func1(nums)
    else:
        return func2(nums)


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]


print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]