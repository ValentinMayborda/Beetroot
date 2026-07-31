# WRONG!!!
# def add_curse(student, courses=[]):
#     courses.append(student)
#     return courses
#
#
# print(add_curse('Vova', ['Python']))
# print(add_curse('Alina'))
# print(add_curse('Valentin'))
# print(add_curse('Roana'))
# #
# # ['Python', 'Vova']
# # ['Alina']
# # ['Alina', 'Valentin']
# # ['Alina', 'Valentin', 'Roana']


# CORRECT!
def add_curse(student, courses=None):
    if courses is None:
        courses = []
    courses.append(student)
    return courses

print(add_curse('Vova', ['Python']))
print(add_curse('Alina'))
print(add_curse('Valentin'))
print(add_curse('Roana'))