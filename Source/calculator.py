def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    z = round(y / x, 7)
    return z


def square(x):
    return x * x


def square_root(x):
    z = round(x ** (1 / 2), 7)
    return z


class Calculate:
    result = 0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = addition(x, y)
        return self.result

    def subtract(self, x, y):
        self.result = subtraction(x, y)
        return self.result

    def multiply(self, x, y):
        self.result = multiplication(x, y)
        return self.result

    def divide(self, x, y):
        self.result = division(x, y)
        return self.result

    def square(self, x):
        self.result = square(x)
        return self.result

    def square_root(self, x):
        self.result = square_root(x)
        return self.result
