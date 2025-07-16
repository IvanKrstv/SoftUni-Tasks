class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = -step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current >= self.count * self.step:
            raise StopIteration
        return self.current

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

