import functools


class Generator:
    def __init__(self, initial: int, factor: int, multiple: int = 1):
        self.initial = initial
        self.factor = factor
        self.current = initial
        self.multiple = multiple
        self.previous = dict()

    def next(self):
        # if self.current in self.previous.keys():
        #     print("HIT!")
        #     return self.previous[self.current]
        value = self.current * self.factor % 2147483647
        # self.previous[self.current] = value
        self.current = value
        return self.current

    def next2(self):
        self.current =self.current * self.factor % 2147483647
        while self.current % self.multiple != 0:
            self.current =self.current * self.factor % 2147483647
        return self.current


class GeneratorA(Generator):
    def __init__(self, initial: int):
        super().__init__(initial, 16807, 4)


class GeneratorB(Generator):
    def __init__(self, initial: int):
        super().__init__(initial, 48271, 8)
