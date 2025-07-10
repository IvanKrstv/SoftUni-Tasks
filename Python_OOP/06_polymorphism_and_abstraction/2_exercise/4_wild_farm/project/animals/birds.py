from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Seed, Meat


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def weight_increment(self) -> float:
        return 0.25

    @property
    def allowed_food(self):
        return [Meat]


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def weight_increment(self) -> float:
        return 0.35

    @property
    def allowed_food(self):
        return [Meat, Vegetable, Fruit, Seed]