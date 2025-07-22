from project.computer_types.computer import Computer

class DesktopComputer(Computer):
    @property
    def available_processors(self):
        return {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800
    }

    @property
    def valid_rams(self):
        return [2**el for el in range(1, 8)]

    def __str__(self):
        return "desktop computer"