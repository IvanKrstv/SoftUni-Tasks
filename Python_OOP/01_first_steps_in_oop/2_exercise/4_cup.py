class Cup:
    def __init__(self, size:int, quantity: int):
        self.quantity = quantity
        self.size = size

    def fill(self, quantity: int):
        if self.size > self.quantity + quantity:
            self.quantity += quantity

    def status(self):
        return self.size - self.quantity

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
