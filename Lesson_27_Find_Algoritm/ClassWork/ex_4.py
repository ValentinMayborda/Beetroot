# sqrt(n)
# # O(sqrt(n))
import math


class JumpSearch:
    def __init__(self, data):
        self.data = sorted(data)

    def search(self, target):
        n = len(self.data)
        step = int(math.sqrt(n))
        prev = 0
        # Стрибки блоками
        while prev < n and self.data[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        # Лінійний пошук у знайденому блоці
        for i in range(prev, min(step, n)):
            if self.data[i] == target:
                return i
        return -1


if __name__ == "__main__":
    array = [5, 3, 8, 1, 9, 2]

    searcher = JumpSearch(array)
    target = 8
    result = searcher.search(target)
    if result != -1:
        print(f"Element {target} found at index {result} in the sorted array: {searcher.data}")
    else:
        print(f"Element {target} not found in the array")
