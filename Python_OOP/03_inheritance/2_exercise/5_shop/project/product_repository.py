from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = next((p for p in self.products if p.name == product_name), None)
        if product is not None:
            return product

    def remove(self, product_name: str):
        product = next((p for p in self.products if p.name == product_name), None)
        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        info = ''
        for product in self.products:
            info += f'{product.name}: {product.quantity}\n'
        return info.rstrip('\n')