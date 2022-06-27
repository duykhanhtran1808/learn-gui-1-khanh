def add(*args):
    total = 0
    for n in args:
        total += n
    return total


result = add(1, 2, 3, 4, 5)
print(result)


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(model="G6")
print(my_car.make)
