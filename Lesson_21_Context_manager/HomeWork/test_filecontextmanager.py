import unittest
import os
from task1_filecontextmanager import FileContextManager


class TestFileContextManager(unittest.TestCase):

    def setUp(self):
        self.filename = 'Test_text.txt'
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write('Тестовий текст')


    def test_open_file(self):
        with FileContextManager(self.filename, 'r') as f:
            self.assertIsNotNone(f.closed)


    def test_empty_file(self):
        with FileContextManager(self.filename, "w"):
            pass

        with FileContextManager(self.filename, "r") as f:
            self.assertEqual(f.read(), "")


    def test_write_read_file(self):
        with FileContextManager(self.filename, 'w') as f:
            f.write('123456789')

        with FileContextManager(self.filename, 'r') as f:
            self.assertEqual(f.read(), '123456789')


    def test_create_new_file(self):
        filename = "new_file.txt"
        if os.path.exists(filename):
            os.remove(filename)

        with FileContextManager(filename, "w") as f:
            f.write("Привіт")

        self.assertTrue(os.path.exists(filename))

        with FileContextManager(filename, "r") as f:
            self.assertEqual(f.read(), "Привіт")

        os.remove(filename)

    def test_counter_increment(self):
        start = FileContextManager.counter
        with FileContextManager(self.filename, 'r'):
            pass

        self.assertEqual(FileContextManager.counter, start + 1)

    def test_file_closed(self):
        with FileContextManager(self.filename, 'r') as f:
            self.assertFalse(f.closed)

        self.assertTrue(f.closed)

    def test_append_file(self):
        with FileContextManager(self.filename, 'a') as f:
            f.write('!!!')

        with FileContextManager(self.filename, 'r') as f:
            self.assertEqual(f.read(), 'Тестовий текст!!!')


if __name__ == '__main__':
    unittest.main()
