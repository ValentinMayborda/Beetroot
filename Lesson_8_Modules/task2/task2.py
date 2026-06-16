import sys

print(sys.path)

#sys.path.append(r'C:\Users\NoName\PycharmProjects\Beetroot\Lesson_8_Modules\task2\dir1')
sys.path.insert(0, 'dir1')

from dir1 import mod
print(sys.path)
mod.hello()



