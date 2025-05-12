# Library System:
# Create classes for Book, Member,
# and Library to manage borrowing and returning books.


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False
#     # def __str__(self):
#         # return f"{self .title} by {self.author}"
# class Member:
#     def __init__(self, name):
#         self.name = name
#         self.borrowed_books = []
#     def borrow_book(self, book):
#         if not book.is_borrowed:
#             book.is_borrowed = True
#             self.borrowed_books.append(book)
#             print(f"{self.name} borrowed '{book.title}'")
#         else:
#             print(f"'{book.title}' is already borrowed.")
#     def return_book(self, book):
#         if book in self.borrowed_books:
#             book.is_borrowed = False
#             self.borrowed_books.remove(book)
#             print(f"{self.name} returned '{book.title}'")
#         else:
#             print(f"{self.name} does not have '{book.title}'")
#     # def __str__(self):
#     #     return f"Member: {self.name}"
# class Library:
#     def __init__(self):
#         self.books = []
#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Added '{book.title}' to the library.")
#     def show_available_books(self):
#         print("Available books:")
#         for book in self.books:
#             if not book.is_borrowed:
#                 print(f" - {book}")
#     # def __str__(self):
#     #     return f"Library with {len(self.books)} books"
#
# library = Library()
# book1 = Book("Man on the car", "Charan")
# book2 = Book("The Robert", "Venu")
# library.add_book(book1)
# library.add_book(book2)
# member1 = Member("John")
# member1.borrow_book(book1)
# member1.return_book(book1)
#
# library.show_available_books()


#Bank Account with Inheritance
# Create a BankAccount base class and derive SavingsAccount and
# CurrentAccount with different interest and withdrawal rules.
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{self.name} deposited ₹{amount}. Balance is now ₹{self.balance}")
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance = amount
#             print(f"{self.name} withdraw ₹{amount}. Balance is now ₹{self.balance}")
#         else:
#             print("Not enough balance!")
# class SavingsAccount(BankAccount):
#     def __init__(self, name, balance):
#         super().__init__(name,balance)
#         self.interest_rate = 0.05
#     def add_interest(self):
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         print(f"Interest ₹{interest} added. Balance is now ₹{self.balance}")
# class CurrentAccount(BankAccount):
#     def __init__(self, name, balance):
#         super().__init__(name, balance)
#         self.over_limit = 1000
#     def withdraw(self, amount):
#         if self.balance + self.over_limit >= amount:
#             self.balance -= amount
#             print(f"{self.name} withdrew ₹{amount}. Balance is now ₹{self.balance}")
#         else:
#             print("over limit exceeded!")
#
# savings = SavingsAccount("John", 1000)
# savings.deposit(500)
# savings.add_interest()
# savings.withdraw(200)
# print()
# current = CurrentAccount("raj", 500)
# current.withdraw(1200)
# current.withdraw(500)

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









