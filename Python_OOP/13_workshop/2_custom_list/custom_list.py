from copy import deepcopy


class CustomList:
    def __init__(self, *args):
        self.__data = list(args)

    def append(self, value):
        self.__data.append(value)
        return self.__data

    def remove(self, index):
        self._check_index(index)
        return self.__data.pop(index)

    def _check_index(self, index):
        if index < 0 or index >= len(self.__data):
            raise IndexError(f"Index must be between 0 and {len(self.__data) - 1}")

    def get(self, index):
        self._check_index(index)
        return self.__data[index]

    def extend(self, iterable):
        self.__data.extend(iterable)
        return self.__data

    def insert(self, index, value):
        self._check_index(index)
        self.__data.insert(index, value)
        return self.__data

    def pop(self):
        return self.__data.pop()

    def clear(self):
        return self.__data.clear()

    def index(self, value):
        try:
            return self.__data.index(value)
        except ValueError:
            return -1

    def count(self, value):
        return self.__data.count(value)

    def reverse(self):
        return list(reversed(self.__data))

    def copy(self):
        return deepcopy(self.__data)

    def size(self):
        return len(self.__data)

    def add_first(self, value):
        self.__data.insert(0, value)

    def dictionize(self):
        result = {}

        for index in range(0, len(self.__data), 2):
            try:
                result[self.__data[index]] = self.__data[index + 1]
            except IndexError:
                result[self.__data[index]] = ' '

        return result

    def move(self, n):
        first_part = self.__data[:n]
        second_part = self.__data[n:]
        self.__data = second_part + first_part

        return self.__data