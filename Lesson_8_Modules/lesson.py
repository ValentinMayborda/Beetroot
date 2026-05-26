import os, sys
from mod import sum_
import mod
print(__file__) # адреса фалу
print(f'Lesson_9^, {__name__}') # назва фалу main

print(sys.path)
#sys.path.append(r'W:\sdasd\dsd\dddd\my_lib.py') #Додати посилання на свою бібліотеку


if __name__ == '__main__':
    #mod.sum_(5, 5)
    print(mod.sum_(5, 5))
    print(sum_(5, 5))
    print("Точка входу")