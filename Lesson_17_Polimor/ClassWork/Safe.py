# Створіть клас Safe, який представляє сейф з кодом. Він повинен мати:

# ●  __code (приватний): код сейфа (рядок).

# ● __max_attempts (приватний): максимальна кількість спроб введення коду.

# ● _attempts_left (захищений)

# ● _is_open (захищений)

# Реалізуйте методи:
# ● try_open(code)
# ● is_open()

class Safe:
    def __init__(self, code: str, max_attempts: int = 3):
        self.__code = code
        self.__max_attempts = max_attempts
        self._attempts_left = max_attempts
        self._is_open = False

    def try_open(self, code):
        if self._is_open:
            return True

        if self._attempts_left <= 0:
            return False

        if code == self.__code:
            self._is_open = True
            return True
        else:
            self._attempts_left -= 1
            return False

    def is_open(self) -> bool:
        return self._is_open


safe = Safe("4569", 2)
print(safe.try_open('0000'))
print(safe.try_open('4569'))

print(safe.is_open())
