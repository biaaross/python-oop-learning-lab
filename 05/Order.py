from dataclasses import dataclass, field
import uuid


@dataclass
class Order:
    customer: object
    products: list = field(default_factory=list)

    order_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    _total_price: float = field(init=False, default=0.0)

    def calculate_total(self):
        self._total_price = sum(product.price for product in self.products)
        return self._total_price

    @property
    def total_price(self):
        return self._total_price

    def add_product(self, product):
        self.products.append(product)
        self.calculate_total()
        return "Product added to order."

    def remove_product(self, product):
        if product not in self.products:
            return "Product not found in order."

        self.products.remove(product)
        self.calculate_total()
        return "Product removed from order."