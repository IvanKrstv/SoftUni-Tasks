from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        valid_types = {'Chair', 'HobbyHorse'}
        if product_type not in valid_types:
            raise Exception("Invalid product type!")

        if product_type == 'Chair':
            product = Chair(model, price)
        else:
            product = HobbyHorse(model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        valid_types = {'FurnitureStore', 'ToyStore'}
        if store_type not in valid_types:
            raise Exception(f"{store_type} is an invalid type of store!")

        if store_type == 'FurnitureStore':
            store = FurnitureStore(name=name, location=location)
        else:
            store = ToyStore(name=name, location=location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        type_mapping = {
            'FurnitureStore': 'Furniture',
            'ToyStore': 'Toys'
        }

        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        purchased_products = []
        for product in products:
            if product.sub_type == type_mapping[store.__class__.__name__]:
                purchased_products.append(product)
                store.products.append(product)
                self.products.remove(product)
        store.capacity -= len(purchased_products)
        self.income += sum(p.price for p in purchased_products)

        if purchased_products:
            return f"Store {store.name} successfully purchased {len(purchased_products)} items."
        else:
            return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."
        else:
            self.stores.remove(store)
            return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        discounted_elements = 0
        for product in self.products:
            if product.model == product_model:
                product.discount()
                discounted_elements += 1

        return f"Discount applied to {discounted_elements} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)

        if not store:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        info = (f"Factory: {self.name}\n"
                f"Income: {self.income:.2f}\n"
                f"***Products Statistics***\n"
                f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}\n")

        products_dict = {product.model: [p for p in self.products if p.model == product.model] for product in self.products}
        for model, products in sorted(products_dict.items(), key=lambda x: x[0]):
            info += f'{model}: {len(products)}\n'

        info += f"***Partner Stores: {len(self.stores)}***\n"
        for store in self.stores:
            info += f'{store.name}\n'

        return info.strip()


# Initialize the FactoryManager
factory_manager = FactoryManager("Cool Factory")

# Produce some items
print(factory_manager.produce_item("Chair", "Classic", 80.0))
print(factory_manager.produce_item("Chair", "Modern", 100.0))
print(factory_manager.produce_item("Chair", "Modern", 200.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 120.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 100.0))
print()

# Register new stores
print(factory_manager.register_new_store("FurnitureStore", "Furniture Outlet", "SOF"))
print(factory_manager.register_new_store("ToyStore", "Toy World", "VAR"))
print()

# Sell products to stores
chair1 = factory_manager.products[0]
chair2 = factory_manager.products[1]
chair3 = factory_manager.products[2]
store1 = factory_manager.stores[0]
store2 = factory_manager.stores[1]
print(factory_manager.sell_products_to_store(store2, chair1, chair2))
print(factory_manager.sell_products_to_store(store1, chair1, chair2, chair3))
print()

# Unregister store
print(factory_manager.unregister_store("Furniture Outlet"))
print()

# Discount products
print(factory_manager.discount_products("Classic"))
print(factory_manager.discount_products("Rocking Horse"))
print()

# Request store statistics
print(factory_manager.request_store_stats("Furniture Outlet"))
print(factory_manager.request_store_stats("Toy World"))
print()

# Factory statistics
print(factory_manager.statistics())
print()

# Unregister store
print(factory_manager.unregister_store("Toy World"))

