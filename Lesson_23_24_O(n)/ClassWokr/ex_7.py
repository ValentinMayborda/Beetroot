# O(n!) - Факторійна складність
def generate_permutations(arr):
    if len(arr) == 1:
        return [arr[:]]
    permutations = []
    for i in range(len(arr)):
        remaining_elements = arr[:i] + arr[i + 1:]
        for permutation in generate_permutations(remaining_elements):
            permutations.append([arr[i]] + permutation)
    return permutations

arr = [1, 2, 3]
print(generate_permutations(arr))  # O(n!)
# n = 5: 5! = 120 операцій
# n = 10: 10! = 3 628 800
# n = 20: 20! = 2 432 902 008 176 640 000