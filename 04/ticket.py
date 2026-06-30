import uuid


class Ticket:
    def __init__(self, customer, movie, price):
        self.ticket_id = str(uuid.uuid4())
        self.customer = customer
        self.movie = movie
        self.__price = price

    # ---------------- PRICE ACCESS ----------------

    @property
    def price(self):
        return self.__price

    # ---------------- STRING REPRESENTATION ----------------

    def __str__(self):
        return f"{self.customer} | ({self.movie}) | {self.price} €"