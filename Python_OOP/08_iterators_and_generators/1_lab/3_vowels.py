VOWELS = "aeiouAEIOU"

class vowels:
    def __init__(self, string: str):
        self.string = string

    def __iter__(self):
        return self

    def __next__(self):
        if self.string:
            temp = self.string[0]
            self.string = self.string[1:]
            if temp in VOWELS:
                return temp
            else:
                return
        else:
            raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)