from time import time
import resource

# def read_file(file_name):
#     text_file = open(file_name, 'r')
#     lines = text_file.readlines()
#     text_file.close()
#     return lines
#
# start = time()
# data = read_file('data.txt')
# print(time() - start)
# print('Peak memory usage: ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, ' bytes')

def read_file_yield(filename):
    with open(filename, 'r') as text_file:
        while True:
            line = text_file.readline()
            if not line:
                break
            yield line.rstrip()

# start = time()
# data = read_file_yield('data.txt')
# print(time() - start)
# print('Peak memory usage: ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, ' bytes')

# 216 723 456 bytes 0.45s 206Mb

# 23 187 456 bytes 0.00s  23Mb
# 23 482 368

def read_file_simple(filename):
    with open(filename, 'r') as text_file:
        yield from text_file

start = time()
data = read_file_simple('data.txt')
print(time() - start)
print('Peak memory usage: ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, ' bytes')


def search_in_file(filename, keyword):
    for i, line in enumerate(read_file_yield(filename)):
        if keyword in line:
            yield i, line