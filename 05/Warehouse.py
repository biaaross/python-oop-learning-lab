from dataclasses import dataclass, field
import uuid

@dataclass
class Warehouse:
    warehouse_name: str
    location: str
    products: list = field(default_factory=list)
    warehouse_id: str = field(default_factory=lambda : str(uuid.uuid4()))

    def add_product(self, product):
        self.products.append(product)
        return "Product added successfully."

    def remove_product(self, product):
        if product not in self.products:
            return "Product not found."

        self.products.remove(product)
        return "Product removed successfully." 
