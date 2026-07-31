# __iter__
# for x in my_list
# my_list.__iter__()
my_list = [1, 2, 3]

iterator_from_list = iter(my_list)
my_list.__iter__()

# __next__ i __iter__

book_mark = iter(my_list)
print(next(book_mark))
print(next(book_mark))
print(next(book_mark))
print(next(book_mark))