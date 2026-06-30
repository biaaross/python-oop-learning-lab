from cinema import Cinema
from movie import Movie
from customer import Customer
from ticket import Ticket


def main():
    cinema = Cinema("My Cinema")

    while True:
        print("\n" + "=" * 40)
        print("        CINEMA MANAGEMENT SYSTEM")
        print("=" * 40)

        print("1. Add Movie")
        print("2. List Movies")
        print("3. Remove Movie")

        print("4. Add Customer")
        print("5. List Customers")

        print("6. Sell Ticket")
        print("7. Cancel Ticket")

        print("8. Show Transactions")
        print("0. Exit")

        choice = input("\nSelect option: ")

        # ---------------- ADD MOVIE ----------------
        if choice == "1":
            title = input("Title: ")
            duration = int(input("Duration (min): "))
            genre = input("Genre: ")
            seats = int(input("Total Seats: "))

            movie = Movie(title, duration, genre, seats)
            print(cinema.add_movie(movie))

        # ---------------- LIST MOVIES ----------------
        elif choice == "2":
            movies = cinema.list_movies()
            for m in movies:
                print(m)

        # ---------------- REMOVE MOVIE ----------------
        elif choice == "3":
            movie_id = input("Movie ID: ")
            print(cinema.remove_movie(movie_id))

        # ---------------- ADD CUSTOMER ----------------
        elif choice == "4":
            name = input("Customer Name: ")
            customer = Customer(name)
            print(cinema.add_customer(customer))

        # ---------------- LIST CUSTOMERS ----------------
        elif choice == "5":
            for c in cinema.list_customers():
                print(c)

        # ---------------- SELL TICKET ----------------
        elif choice == "6":
            customer_id = input("Customer ID: ")
            movie_id = input("Movie ID: ")

            print(cinema.sell_ticket(customer_id, movie_id))

        # ---------------- CANCEL TICKET ----------------
        elif choice == "7":
            ticket_id = input("Ticket ID: ")
            print(cinema.cancel_ticket(ticket_id))

        # ---------------- TRANSACTIONS ----------------
        elif choice == "8":
            for t in cinema.show_transactions():
                print(t)

        # ---------------- EXIT ----------------
        elif choice == "0":
            print("Exiting system...")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()