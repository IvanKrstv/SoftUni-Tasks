from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=50)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        info = (f'Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n'
                f'{self.get_estimated_profit()}\n'
                f'**Furniture for sale:\n')
        products_dict = {product.model: [p for p in self.products if p.model == product.model] for product in self.products}
        for model, products in sorted(products_dict.items(), key=lambda x: x[0]):
            average_price = sum(p.price for p in products) / len(products) if products else 0
            info += f'{model}: {len(products)}pcs, average price: {average_price:.2f}\n'

        return info.strip()
