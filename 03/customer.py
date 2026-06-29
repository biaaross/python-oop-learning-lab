import uuid

class Customer:
    def __init__(self, name):
        self.customer_id = str(uuid.uuid4())
        self.name = name

        self.rented_cars = []
        
        self._transactions = []


    def rent_car(self, car):
        if car.is_rented:
            return "Car is already rented."

        car.mark_as_rented()
        self.rented_cars.append(car)

        self._transactions.append(
            f"RENT: {car.brand} {car.model} ({car.vehicle_id})"
        )
        return "Car rented successfully."


    def return_car(self, car):
        
        if car not in self.rented_cars:
            return "This car does not belong to customer."

        car.return_car()
        self.rented_cars.remove(car)

        self._transactions.append(
            f"RETURN: {car.brand} {car.model} ({car.vehicle_id})"
        )

        return "Car returned successfully."
    

    def show_transactions(self):
        for t in self._transactions:
            print(t)


    def get_rented_cars(self):
        return self.rented_cars


    def __str__(self):
        return f"Customer: {self.name} | ID: {self.customer_id}"