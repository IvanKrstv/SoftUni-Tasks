from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.tiger import Tiger
from project.lion import Lion
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker is None:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_care = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= animal_care:
            self.__budget -= animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        info = f'You have {len(self.animals)} animals\n'
        # lions, tigers, cheetahs = [], [], []
        # for animal in self.animals:
        #     if animal.__class__.__name__ == 'Lion':
        #         lions.append(animal)
        #     elif animal.__class__.__name__ == 'Tiger':
        #         tigers.append(animal)
        #     else:
        #         cheetahs.append(animal)
        info += self.add_info('a', self.animals)
        return info.rstrip('\n')

    def workers_status(self):
        info = f'You have {len(self.workers)} workers\n'
        # keepers, caretakers, vets = [], [], []
        # for worker in self.workers:
        #     if worker.__class__.__name__ == 'Keeper':
        #         keepers.append(worker)
        #     elif worker.__class__.__name__ == 'Caretaker':
        #         caretakers.append(worker)
        #     else:
        #         vets.append(worker)
        info += self.add_info('w',self.workers)
        return info.rstrip('\n')

    @staticmethod
    def add_info(category:str, lst: list[Animal | Worker]):
        current_dict = {'Lion':[], 'Tiger':[], 'Cheetah':[]} if category == 'a' else {'Keeper':[], 'Caretaker':[], 'Vet':[]}
        for el in lst:
            name_key = el.__class__.__name__
            current_dict[name_key].append(el)

        info = ''
        for key, items in current_dict.items():
            info += f'----- {len(items)} {key}s:\n'
            for el in items:
                info += f'{el}\n'
        return info


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())