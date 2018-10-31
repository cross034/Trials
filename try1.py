# Observer pattern


class IntObserver:
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.fn_list = []

    def attach(self, fn):
        self.fn_list.append(fn)
        print(self.fn_list)

    def set(self, other):
        self.value = other
        for fn in self.fn_list:
            fn(other)

    def __str__(self):
        return str(self.value)


num1 = IntObserver(1)
print(num1)


def foo(value):
    print("Value changed to {}".format(value))


num1.attach(foo)

num1.set(2)
