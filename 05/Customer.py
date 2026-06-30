from dataclasses import dataclass, field

from base_user import BaseUser


@dataclass
class Customer(BaseUser):
    orders: list = field(default_factory=list)

    def place_order(self, order):
        self.orders.append(order)
        return "Order placed successfully."

    def cancel_order(self, order):
        if order not in self.orders:
            return "Order not found."

        self.orders.remove(order)
        return "Order cancelled successfully."