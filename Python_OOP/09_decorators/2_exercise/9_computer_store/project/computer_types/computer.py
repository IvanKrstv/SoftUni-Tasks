from abc import ABC, abstractmethod
from math import log


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value == '' or value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value == '' or value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def valid_rams(self):
        pass

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {str(self)} {self.manufacturer} {self.model}!")
        if ram not in self.valid_rams:
            raise ValueError(f"{ram}GB RAM is not compatible with {str(self)} {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price = int(log(ram, 2) * 100 + self.available_processors[processor])
        return f"Created {self.__repr__()} for {self.price}$."

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"