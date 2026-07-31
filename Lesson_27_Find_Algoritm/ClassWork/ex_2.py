class LinearSearch:
    def __init__(self, data):
        self.data = data

    def search(self, target):
        for i in range(len(self.data)):
            if self.data[i] == target:
                return i
        return -1

if __name__ == "__main__":
    array = [5, 3, 8, 1, 9, 2]
    searcher = LinearSearch(array)
    target = 8
    result = searcher.search(target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")