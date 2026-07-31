import os
from datetime import datetime
import logging
from typing import Dict, List


class FileManager:
    def __init__(self, filename: str, mode: str = 'r', encoding: str = 'utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
        self.start_time = None
        self.operations_count = 0

        # Налаштування логування
        logging.basicConfig(
            filename='file_operations.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

        # Статистика операцій
        self.stats: Dict[str, int] = {
            'reads': 0,
            'writes': 0,
            'errors': 0
        }

    def __enter__(self) -> 'FileManager':
        try:
            self.file = open(self.filename, self.mode, encoding=self.encoding)
            self.start_time = datetime.now()
            self._log_operation('opened')
            return self
        except Exception as e:
            self._handle_error(f'Error opening file: {e}')
            raise

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        try:
            if self.file:
                self.file.close()
                self._log_operation('closed')
                duration = (datetime.now() - self.start_time).total_seconds()
                self._save_session_stats(duration)
            return False
        except Exception as e:
            self._handle_error(f'Error closing file: {e}')
            return False

    def read_file(self) -> List[str]:
        try:
            lines = self.file.readlines()
            self.stats['reads'] += len(lines)
            self._log_operation(f'read {len(lines)} lines')
            return lines
        except Exception as e:
            self._handle_error(f'Error reading file: {e}')
            return []

    def write_file(self, content: str) -> bool:
        try:
            self.file.write(content + "\n")
            self.stats['writes'] += 1
            self._log_operation('wrote line')
            return True
        except Exception as e:
            self._handle_error(f'Error writing file: {e}')
            return False

    def get_size(self) -> int:
        try:
            return os.path.getsize(self.filename)
        except Exception as e:
            self._handle_error(f'Error getting file size: {e}')
            return 0

    def get_stats(self) -> Dict[str, int]:
        return self.stats.copy()

    def _log_operation(self, operation: str) -> None:
        self.operations_count += 1
        logging.info(f'File {self.filename} - Operation: {operation}')

    def _handle_error(self, error_message: str) -> None:
        self.stats['errors'] += 1
        logging.error(error_message)

    def _save_session_stats(self, duration: float) -> None:
        stats_file = 'session_stats.log'
        try:
            with open(stats_file, 'a', encoding='utf-8') as f:
                stats = (
                    f"\nSession {datetime.now()}\n"
                    f"File: {self.filename}\n"
                    f"Duration: {duration:.2f} seconds\n"
                    f"Operations: {self.operations_count}\n"
                    f"Reads: {self.stats['reads']}\n"
                    f"Writes: {self.stats['writes']}\n"
                    f"Errors: {self.stats['errors']}\n"
                    f"{'-' * 30}"
                )
                f.write(stats)
        except Exception as e:
            logging.error(f'Error saving session stats: {e}')

if __name__ == '__main__':
    with FileManager('test.txt', 'w') as fm:
        fm.write_file('Hello, world!')
        fm.write_file('This is a test.')
        print(f"File size: {fm.get_size()} bytes")
        print(f"Operations: {fm.get_stats()}")

    with FileManager('test.txt', 'r') as fm:
        lines = fm.read_file()
        print(f"Read {len(lines)} lines:")
        print(f"Final stats: {fm.get_stats()}")
        print(f"File size: {fm.get_size()} bytes")