# Movie Ticket Booking System
# Classes: Movie, Theater, Showtime, User.
# Implement seat selection and booking confirmation
class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Theater:
    def __init__(self, name, total_seats=20):
        self.name = name
        self.total_seats = total_seats

class Showtime:
    def __init__(self, movie, theater, time):
        self.movie = movie
        self.theater = theater
        self.time = time
        self.booked_seats = set()

    def book_seats(self, seat_numbers):
        for seat in seat_numbers:
            if seat in self.booked_seats:
                print(f"Seat {seat} is already booked!")
                return False
        self.booked_seats.update(seat_numbers)
        return True

    def display_seats(self):
        print("Available seats:")
        for seat in range(1, self.theater.total_seats + 1):
            status = "X" if seat in self.booked_seats else str(seat)
            print(status, end=" ")
        print()

class User:
    def __init__(self, name):
        self.name = name

    def book_ticket(self, showtime, seats):
        if showtime.book_seats(seats):
            print(f"Booking confirmed for {self.name}")
            print(f"Movie: {showtime.movie.title}")
            print(f"Theater: {showtime.theater.name}")
            print(f"Time: {showtime.time}")
            print(f"Seats: {seats}")
        else:
            print("Booking failed.")


movie1 = Movie("Interstellar", 169)
theater1 = Theater("IMAX", total_seats=10)
showtime1 = Showtime(movie1, theater1, "7:30 PM")

user1 = User("John")

showtime1.display_seats()
# seats_to_book = [3,4]
seats_to_book = list(map(int, input("Enter seat numbers: ").split(',')))
user1.book_ticket(showtime1, seats_to_book)

showtime1.display_seats()









