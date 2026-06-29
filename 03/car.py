import uuid

class Car:
    def __init__(self, brand, model, year, daily_price):
        self.vehicle_id = str(uuid.uuid4())
        
        self.brand = brand
        self.model = model
        self.year = year
        
        self.__daily_price = daily_price
        
        self.is_rented = False

    
    def mark_as_rented(self):
        if self.is_rented:
            return "Vehicle already rented."

        self.is_rented = True
        return "Vehicle rented successfully."
        

    def return_car(self):
        if not self.is_rented:
            return "Vehicle is not currently rented."

        self.is_rented = False
        return "Vehicle returned successfully."
    

    def get_price(self):
        return self.__daily_price
    

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"