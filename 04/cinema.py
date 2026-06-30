import uuid
from ticket import Ticket

class Cinema():
    def __init__(self, name):
        self.cinema_id = str(uuid.uuid4())
        self.name = name

        self.movies = []
        self.customers = []
        self.tiskets = []
        self._transaction_history = []

    # ---------------- MOVIES ----------------

    def add_movie(self, movie):
        for m in self.movies:
            if movie.movie_id == m.movie_id:
                return "Movie Already Exists"

        self.movies.append(movie)
        return "Movie Added Succesfully"

    def remove_movie(self, movie_id):
        for m in self.movies:
            if m.movie_id == movie_id:
                self.movies.remove(m)
                return "Movie Deleted Successfully"

        return "Movie Not Found"

    def list_movies(self):
        return self.movies

    # ---------------- CUSTOMERS ----------------

    def add_customer(self, customer):
        for c in self.customers:
            if c.customer_id == customer.customer_id:
                return "Customer Already Exists"

            self.customers.append(customer)
            return "Customer Added Succesfully"

    def list_customers(self):
        return self.customers

    # ---------------- TICKET SYSTEM ----------------

    def sell_ticket(self, customer_id, movie_id):

        customer = self._find_customer(customer_id)
        movie = self._find_movie(movie_id)

        if customer is None:
            return "Customer Not Found"

        if movie is None:
            return "Movie Not Found"

        if movie.available_seats <= 0:
            return "No Available Seats"

        movie.reserve_seat()

        ticket = Ticket(customer, movie, movie.get_price())

        self.tiskets.append(ticket)
        customer.purchased_tickets.append(ticket)

        log = f"TICKET SOLD | Customer: {customer.name} | Movie: {movie.title}"
        self._transaction_history.append(log)

        return "Ticket Sold Successfully"

    def cancel_ticket(self, ticket_id):

        ticket = self._find_ticket(ticket_id)

        if ticket is None:
            return "Ticket Not Found"

        movie = ticket.movie
        customer = ticket.customer

        movie.cancel_reservation()

        if ticket in customer.purchased_tickets:
            customer.purchased_tickets.remove(ticket)

        self.tiskets.remove(ticket)

        log = f"TICKET CANCELLED | Customer: {customer.name} | Movie: {movie.title}"
        self._transaction_history.append(log)

        return "Ticket Cancelled Successfully"

    # ---------------- FINDERS ----------------

    def _find_movie(self, movie_id):
        for m in self.movies:
            if m.movie_id == movie_id:
                return m
        return None

    def _find_customer(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                return c
        return None

    def _find_ticket(self, ticket_id):
        for t in self.tiskets:
            if t.ticket_id == ticket_id:
                return t
        return None

    # ---------------- LOGS ----------------

    def show_transactions(self):
        return self._transaction_history

    def __str__(self):
        return f"Cinema: {self.name}"