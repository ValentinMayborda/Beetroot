class InterpolationSearch:
    def __init__(self, data):
        self.data = sorted(data)

    def search(self, target):
        low = 0
        high = len(self.data) - 1
        while low <= high and target >= self.data[low] and target <= self.data[high]:
            if low == high:
                if self.data[low] == target:
                    return low
                return -1
            pos = low + int(
                (target - self.data[low]) * (high - low) / (self.data[high] - self.data[low])
            )
            if self.data[pos] == target:
                return pos
            elif self.data[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        return -1


if __name__ == "__main__":
    array = [5, 3, 8, 1, 9, 2]

    searcher = InterpolationSearch(array)
    target = 8
    result = searcher.search(target)
    if result != -1:
        print(f"Element {target} found at index {result} in the sorted array: {searcher.data}")
    else:
        print(f"Element {target} not found in the array")

# [10, 20, 30, 40, 50, 60, 70, 80, 100000000]; шукаємо: 70
# 40 -> 60 -> 70 - binary search
# O(n)

