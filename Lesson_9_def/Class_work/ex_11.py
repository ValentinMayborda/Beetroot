# [4, 5, 6, 5, 4, 3, 4, 3, 3, 3]

def sort_by_frequency(lst):
    return sorted(lst, key=lambda x: lst.count(x))

print(sort_by_frequency([4, 5, 6, 5, 4, 3, 4, 3, 3, 3, 8, 4, 3]))