from project.computer_types.computer import Computer
from math import log


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800
    }
    VALID_RAMS = [2**el for el in range(1, 8)]

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram not in self.VALID_RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price = int(log(ram, 2) * 100 + self.AVAILABLE_PROCESSORS[processor])
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."