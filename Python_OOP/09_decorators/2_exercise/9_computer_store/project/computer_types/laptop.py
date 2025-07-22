from project.computer_types.computer import Computer
from math import log


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }
    VALID_RAMS = [2**el for el in range(1, 7)]

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram not in self.VALID_RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price = int(log(ram, 2) * 100 + self.AVAILABLE_PROCESSORS[processor])
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."