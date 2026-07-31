# yield from
def chain_generator(*iterables):
    for it in iterables:
        yield from it  # for x in it: yield x

result = list(chain_generator([1, 2, 3], [4, 5], [6, 7, 8]))
print(result)