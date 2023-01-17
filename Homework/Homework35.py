class Power:
    def __init__(self, num):
        self.num = num

    def __call__(self, fn):
        self.fn = fn

        def wrap(a, b):
            return f"Результат: {fn(a, b) ** self.num}"

        return wrap


@Power(3)
def calc(a, b):
    return a * b


print(calc(2, 2))

