VOWELS = "aeiouy"

class vowels:
    def __init__(self, string: str):
        self.string = string
        self.index = -1
        self.vowels = [el for el in self.string if el.lower() in VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        # self.index += 1
        # if self.index >= len(self.string):
        #     raise StopIteration
        # if self.string[self.index] in VOWELS:
        #     return self.string[self.index]
        # return self.__next__()

        self.index += 1
        if self.index >= len(self.vowels):
            raise StopIteration
        return self.vowels[self.index]

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)