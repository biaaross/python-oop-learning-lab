from car import Car
from customer import Customer
from rental_company import RentalCompany


def main():
    company = RentalCompany("DriveNow")

    while True:
        print("\n====== VEHICLE RENTAL SYSTEM ======")
        print("1. Add Car")
        print("2. Add Customer")
        print("3. List Cars")
        print("4. List Customers")
        print("5. Rent Car")
        print("6. Return Car")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            brand = input("Brand: ")
            model = input("Model: ")
            year = input("Year: ")
            price = float(input("Daily Price: "))

            car = Car(brand, model, year, price)
            company.add_car(car)

            print("Vehicle successfully added.")

        elif choice == "2":
            name = input("Customer Name: ")
            customer = Customer(name)
            company.add_customer(customer)

            print("Customer registered.")

        elif choice == "3":
            for car in company.list_cars():
                print(car)

        elif choice == "4":
            for customer in company.list_customers():
                print(customer)

        elif choice == "5":
            customer_id = input("Customer ID: ")
            car_id = input("Car ID: ")

            customer = company.get_customer(customer_id)
            car = company.get_car(car_id)

            if not customer or not car:
                print("Invalid customer or vehicle ID.")
            else:
                print(customer.rent_car(car))

        elif choice == "6":
            customer_id = input("Customer ID: ")
            car_id = input("Car ID: ")

            customer = company.get_customer(customer_id)
            car = company.get_car(car_id)

            if not customer or not car:
                print("Invalid customer or vehicle ID.")
            else:
                print(customer.return_car(car))

        elif choice == "7":
            print("System shutting down...")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()