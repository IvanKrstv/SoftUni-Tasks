class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.current = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.end:
            raise StopIteration
        return self.current

        # if self.start <= self.end:
        #     temp = self.start
        #     self.start += 1
        #     return temp
        # else:
        #     raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)