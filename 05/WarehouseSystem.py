from dataclasses import dataclass, field
import uuid


@dataclass
class WarehouseSystem:
    warehouses: list = field(default_factory=list)
    orders: list = field(default_factory=list)
    shipments: list = field(default_factory=list)

    system_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    _transaction_history: list = field(default_factory=list)


    def add_warehouse(self, warehouse):
        self.warehouses.append(warehouse)
        self._transaction_history.append(f"Warehouse added: {warehouse.warehouse_name}")
        return "Warehouse added successfully."

    def remove_warehouse(self, warehouse):
        if warehouse not in self.warehouses:
            return "Warehouse not found."

        self.warehouses.remove(warehouse)
        self._transaction_history.append(f"Warehouse removed: {warehouse.warehouse_name}")
        return "Warehouse removed successfully."


    def create_order(self, order):
        self.orders.append(order)
        self._transaction_history.append(f"Order created: {order.order_id}")
        return "Order created successfully."

    def cancel_order(self, order):
        if order not in self.orders:
            return "Order not found."

        self.orders.remove(order)
        self._transaction_history.append(f"Order cancelled: {order.order_id}")
        return "Order cancelled successfully."


    def create_shipment(self, shipment):
        self.shipments.append(shipment)
        self._transaction_history.append(f"Shipment created: {shipment.tracking_number}")
        return "Shipment created successfully."

    def update_shipment_status(self, shipment, status: str):
        if shipment not in self.shipments:
            return "Shipment not found."

        shipment.status = status
        self._transaction_history.append(
            f"Shipment updated: {shipment.tracking_number} → {status}"
        )
        return "Shipment status updated."

    
    def show_history(self):
        return self._transaction_history


    def __str__(self):
        return (
            f"WarehouseSystem ID: {self.system_id}\n"
            f"Warehouses: {len(self.warehouses)}\n"
            f"Orders: {len(self.orders)}\n"
            f"Shipments: {len(self.shipments)}"
        )