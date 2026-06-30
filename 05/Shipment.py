from dataclasses import dataclass, field
import uuid


@dataclass
class Shipment:
    order: object 
    tracking_number: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: str = field(default="preparing")  

    def ship(self):
        if self.status != "preparing":
            return "Shipment already processed."

        self.status = "shipped"
        return "Shipment has been shipped."

    def deliver(self):
        if self.status != "shipped":
            return "Shipment cannot be delivered yet."

        self.status = "delivered"
        return "Shipment delivered successfully."

    def __str__(self):
        return f"Tracking: {self.tracking_number} | Status: {self.status}"