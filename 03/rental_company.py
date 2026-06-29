import uuid

class RentalCompany:
    def __init__(self, name):
        self.company_id = str(uuid.uuid4())
        self.name = name

        self.cars = []
        self.customers = []
        self._transactions = []


    def add_car(self, car):
        self.cars.append(car)
        return f"{car} added to fleet."


    def list_cars(self):
        return self.cars


    def get_available_cars(self):
        return [car for car in self.cars if not car.is_rented]


    def get_rented_cars(self):
        return [car for car in self.cars if car.is_rented]


    def add_customer(self, customer):
        self.customers.append(customer)
        return f"{customer.name} added as customer."


    def list_customers(self):
        return self.customers


    def get_car(self, car_id):
        for car in self.cars:
            if car.vehicle_id == car_id:
                return car
        return None


    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None