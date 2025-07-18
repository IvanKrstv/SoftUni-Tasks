class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_items = list(dict_obj.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.dict_items):
            raise StopIteration
        return self.dict_items[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
