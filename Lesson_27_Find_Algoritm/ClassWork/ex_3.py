class BinarySearch:
    def __init__(self, data):
        self.data = sorted(data)

    def search(self, target):
        left, right = 0, len(self.data) - 1

        while left <= right:

            mid = (left + right) // 2  # Знаходимо середину

            if self.data[mid] == target:
                return mid  # Знайдено

            elif self.data[mid] < target:
                left = mid + 1  # Шукати в правій частині

            else:
                right = mid - 1   # Шукати в лівій частині
        return -1

if __name__ == "__main__":
    array = [5, 3, 8, 1, 9, 2]

    searcher = BinarySearch(array)
    target = 8
    result = searcher.search(target)
    if result != -1:
        print(f"Element {target} found at index {result} in the sorted array: {searcher.data}")
    else:
        print(f"Element {target} not found in the array")