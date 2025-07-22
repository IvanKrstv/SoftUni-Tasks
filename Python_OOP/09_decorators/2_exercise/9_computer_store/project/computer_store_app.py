from project.computer_types.computer import Computer
from project.computer_types.laptop import Laptop
from project.computer_types.desktop_computer import DesktopComputer

class ComputerStoreApp:
    VALID_TYPES = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        computer = self.VALID_TYPES[type_computer](manufacturer=manufacturer, model=model)

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
        return f"{computer.__repr__()} sold for {client_budget}$."


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))