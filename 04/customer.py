import uuid


class Customer:
    def __init__(self, name):
        self.customer_id = str(uuid.uuid4())
        self.name = name

        self.purchased_tickets = []
        self.transaction_history = []

    # ---------------- TICKET ACTIONS ----------------

    def buy_ticket(self, ticket):
        self.purchased_tickets.append(ticket)

        self.transaction_history.append(
            f"BUY TICKET | Movie: {ticket.movie.title} | Price: {ticket.price}"
        )

        return "Ticket purchased successfully."

    def cancel_ticket(self, ticket):
        if ticket not in self.purchased_tickets:
            return "Ticket not found."

        self.purchased_tickets.remove(ticket)

        self.transaction_history.append(
            f"CANCEL TICKET | Movie: {ticket.movie.title} | Price: {ticket.price}"
        )

        return "Ticket cancelled successfully."

    # ---------------- HISTORY ----------------

    def show_history(self):
        for t in self.transaction_history:
            print(t)

    # ---------------- STRING ----------------

    def __str__(self):
        return f"Customer: {self.name} | ID: {self.customer_id}"