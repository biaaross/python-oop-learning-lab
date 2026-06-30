from dataclasses import dataclass, field
import uuid


@dataclass
class Product:
    name: str
    quantity: int
    price: float = field(repr=False)  
    product_id: str = field(default_factory=lambda: str(uuid.uuid4()))

 
    @property
    def price(self):
        return self._price

    def __post_init__(self):
 
        self._price = self.price

    def increase_stock(self, amount: int):
        if amount <= 0:
            return "Invalid amount"

        self.quantity += amount
        return "Stock increased"

    def decrease_stock(self, amount: int):
        if amount <= 0:
            return "Invalid amount"

        if self.quantity < amount:
            return "Not enough stock"

        self.quantity -= amount
        return "Stock decreased"

    def __str__(self):
        return f"{self.name} | Stock: {self.quantity}"