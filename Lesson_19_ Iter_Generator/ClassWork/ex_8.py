def infinite_counter(start=0, step=1):
    current = start
    while True:
        yield current
        current += step


counter = infinite_counter(0, 2)
print(next(counter))
print(next(counter))
print(next(counter))