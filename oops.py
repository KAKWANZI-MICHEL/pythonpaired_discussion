
#1.Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

my_car = Car("Toyota", "Red")
print(my_car.brand)
print(my_car.color)

#2.Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. Create an instance of Car and call the method.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print("Engine started!") 

my_car = Car("Toyota", "Red")
my_car.start_engine()

#3.Create a class called BankAccount with attributes account_number and balance. Add methods to:
#Deposit an amount.
#Withdraw an amount (only if sufficient balance exists).
#Print the account balance.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient   funds")

    def print_balance(self):
        print("Account balance:", self.balance)

# Create an account
account = BankAccount(12345, 1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Print balance
account.print_balance()

#4.Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. The Library class should have methods to:
#Add a book to the library.
#Remove a book from the library.
#Check if a book is available by title.
#Borrow a book (mark it as unavailable if it’s available).
#Return a book (mark it as available again if it was borrowed).

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book) 

                break

    def is_available(self, title):
        for book in self.books:
            if book.title == title and book.available:
                return True
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You have borrowed '{title}'") 

                return
        print("Book is not available or not found")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"You   
 have returned '{title}'")
                return
        print("Book is not borrowed or not found")

# Create a library
library = Library()

# Add books
library.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien"))
library.add_book(Book("Pride and Prejudice", "Jane Austen"))

# Check availability by title
print(library.is_available("The Lord of the Rings"))

# Borrow a book
library.borrow_book("The Lord of the Rings")

# Check availability again
print(library.is_available("The Lord of the Rings"))

# Return the book
library.return_book("The Lord of the Rings")