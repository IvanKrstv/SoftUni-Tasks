class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = -1
        self.remaining_steps = number

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        self.remaining_steps -= 1
        if self.remaining_steps < 0:
            raise StopIteration
        if self.index >= len(self.sequence):
            self.index = 0
        return self.sequence[self.index]


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

