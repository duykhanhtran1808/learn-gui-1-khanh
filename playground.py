def add(*args):
    total = 0
    for n in args:
        total += n
    return total


result = add(1, 2, 3, 4, 5)
print(result)
