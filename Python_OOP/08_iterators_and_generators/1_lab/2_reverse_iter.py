class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current_index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index -= 1
        if self.current_index < 0:
            raise StopIteration
        return self.iterable[self.current_index]

        # if self.iterable:
        #     temp = self.iterable[-1]
        #     self.iterable.pop()
        #     return temp
        # else:
        #     raise StopIteration

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)