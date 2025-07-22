from project.computer_types.computer import Computer

class Laptop(Computer):
    @property
    def available_processors(self):
        return {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }

    @property
    def valid_rams(self):
        return [2**el for el in range(1, 7)]

    def __str__(self):
        return "laptop"