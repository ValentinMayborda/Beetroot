# __enter__
# __exit__

class FileWrite:
    def __init__(self, filename):
        self.filename = filename
        self.opened = False
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        self.opened = True
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.opened:
            self.file.close()
        self.opened = False


if __name__ == '__main__':
    with FileWrite('test.txt') as f:
        f.write('Hello, world!\n')
        f.write('Happy end!\n')