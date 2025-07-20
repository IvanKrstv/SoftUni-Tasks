from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=100)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        info = (f'Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n'
                f'{self.get_estimated_profit()}\n'
                f'**Toys for sale:\n')
        toys_dict = {toy.model: [t for t in self.products if t.model == toy.model] for toy in self.products}
        for model, toys in sorted(toys_dict.items(), key=lambda x: x[0]):
            average_price = sum(p.price for p in toys) / len(toys) if toys else 0
            info += f'{model}: {len(toys)}pcs, average price: {average_price:.2f}\n'

        return info.strip()