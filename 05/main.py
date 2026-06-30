from warehouse_system import WarehouseSystem

def main():
    system = WarehouseSystem()

    while True:
        print("\n===== WAREHOUSE SYSTEM =====")
        print("1 - Add Warehouse")
        print("2 - Remove Warehouse")
        print("3 - Create Order")
        print("4 - Create Shipment")
        print("5 - Show History")
        print("0 - Exit")

        choice = input("Select option: ")

        if choice == "0":
            print("Exiting system...")
            break

        elif choice == "1":
            name = input("Warehouse name: ")
            location = input("Location: ")

            from warehouse import Warehouse
            warehouse = Warehouse(name, location)

            print(system.add_warehouse(warehouse))

        elif choice == "2":
            name = input("Warehouse name to remove: ")

            target = None
            for w in system.warehouses:
                if w.warehouse_name == name:
                    target = w
                    break

            if target:
                print(system.remove_warehouse(target))
            else:
                print("Warehouse not found.")

        elif choice == "3":
            from order import Order
            from customer import Customer

            customer_name = input("Customer name: ")
            customer = Customer(customer_name)

            order = Order(customer)

            print(system.create_order(order))

        elif choice == "4":
            from shipment import Shipment

            if not system.orders:
                print("No orders available.")
                continue

            order = system.orders[-1]
            shipment = Shipment(order)

            print(system.create_shipment(shipment))

        
        elif choice == "5":
            for log in system.show_history():
                print(log)

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()