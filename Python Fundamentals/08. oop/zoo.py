class Zoo:
    __animals = 0

    def __init__(self, name):
        self.zoo_name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species: str):
        if species == "mammal":
            result = (
                f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
                f"\nTotal animals: {self.__animals}")
        elif species == "fish":
            result = (
                f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
                f"\nTotal animals: {self.__animals}")
        elif species == "bird":
            result = (
                f"Birds in {self.zoo_name}: {', '.join(self.birds)}"
                f"\nTotal animals: {self.__animals}")

        return result

zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())
for i in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

final_species = input()
print(zoo.get_info(final_species))