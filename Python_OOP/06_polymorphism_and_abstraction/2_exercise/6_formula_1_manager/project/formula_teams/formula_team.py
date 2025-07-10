from abc import ABC, abstractmethod

class FormulaTeam(ABC):
    MIN_BUDGET = 1000000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.MIN_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self) -> dict[str, dict[int, int]]:
        pass

    @property
    @abstractmethod
    def expenses(self) -> int:
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for sponsor, dict_money in self.sponsors.items():
            for place, money in dict_money.items():
                if race_pos <= place:
                    revenue += money
                    break
        revenue -= self.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
