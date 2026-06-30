import uuid


class Movie:
    def __init__(self, title, duration, genre, total_seats):
        self.movie_id = str(uuid.uuid4())
        self.title = title
        self.duration = duration
        self.genre = genre

        self.total_seats = total_seats
        self.available_seats = total_seats

    # ---------------- SEAT MANAGEMENT ----------------

    def reserve_seat(self):
        if self.available_seats <= 0:
            return "No available seats."

        self.available_seats -= 1
        return "Reservation created successfully."

    def cancel_reservation(self):
        if self.available_seats >= self.total_seats:
            return "There is no reservation to cancel."

        self.available_seats += 1
        return "Reservation canceled successfully."

    # ---------------- STRING REPRESENTATION ----------------

    def __str__(self):
        return f"{self.title} ({self.genre}) - {self.duration} min"