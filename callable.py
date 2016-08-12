class Calculator(object):
    def __init__(self, base):
        self.base = base

    def __call__(self, x, y):
        self.base += (x + y)
        return self.base

calculator = Calculator(10)
print(calculator(1, 2)) # calculator.__call__(1, 2)
print(calculator(5, 6))
