from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    @staticmethod
    @abstractmethod
    def make_sound():
        pass