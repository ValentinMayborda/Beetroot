from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwargs):
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler
    finally:
        file_handler.close()


with managed_resource('test.txt', 'r') as f:
    print(f.read())