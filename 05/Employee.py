from dataclasses import dataclass, field
from base_user import BaseUser


@dataclass
class Employee(BaseUser):
    warehouse: list = field(default_factory=list)

    def add_product(self, product):
        self.warehouse.append(product)
        return "Product added successfully."

    def remove_product(self, product):
        if product not in self.warehouse:
            return "Product not found."

        self.warehouse.remove(product)
        return "Product removed successfully."