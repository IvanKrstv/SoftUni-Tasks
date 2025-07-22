from project.computer_types.computer import Computer
from project.computer_types.laptop import Laptop
from project.computer_types.desktop_computer import DesktopComputer

class ComputerStoreApp:
    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        VALID_TYPES = {"Desktop Computer", "Laptop"}
        if type_computer not in VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        if type_computer == 'Laptop':
            computer = Laptop(manufacturer=manufacturer, model=model)
        else:
            computer = DesktopComputer(manufacturer=manufacturer, model=model)

        result = computer.configure_computer(processor=processor, ram=ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = next((comp for comp in self.warehouse if wanted_processor == comp.processor
                    and client_budget >= comp.price
                    and wanted_ram <= comp.ram), None)
        if not computer:
            raise Exception("Sorry, we don't have a computer for you.")
        self.warehouse.remove(computer)
        self.profits += client_budget - computer.price
        return f"{computer} sold for {client_budget}$."


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))