# main.py
from models import LibraryItem, Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 45)
dvd = DVD("Intro to Algorithms", 3, 120)
extra1 = Book("Data Structures", 4, "S. Iyer")
extra2 = Book("Operating Systems", 5, "K. Nair")

alice = Member("Alice", 101)                 # default limit of 3
bob = Member("Bob", 102, max_items=1)

print("=== 0. Abstract class cannot be instantiated ===")
try:
    LibraryItem("x", 99)
except TypeError as e:
    print("TypeError:", e)

print("\n=== 1. Borrowing with error handling ===")
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

print("\n=== 2. Limit and not-borrowed errors ===")
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # Bob's limit is 1
except ValueError as e:
    print("Could not borrow:", e)

try:
    alice.borrow(extra1)
    alice.borrow(extra2)
    print("Alice now has:", alice.borrowed_titles())
    alice.borrow(dvd)  # 4th item -> limit reached
except ValueError as e:
    print("Could not borrow:", e)

try:
    alice.return_item(magazine)  # Alice never borrowed it
except ValueError as e:
    print("Could not return:", e)

print("\n=== 3. Returning with late fees ===")
try:
    fee = alice.return_item(book, days_late=3)
    print(f"Alice returned '{book.title}'. Late fee: Rs {fee}")
    fee = bob.return_item(magazine)
    print(f"Bob returned '{magazine.title}'. Late fee: Rs {fee}")
except ValueError as e:
    print("Could not return:", e)
print("Alice's items:", alice.borrowed_titles())
print("Bob's items:", bob.borrowed_titles())

print("\n=== 4. Polymorphism: one loop, no type checks ===")
for item in [book, magazine, dvd]:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

print("\n=== 5. Class attribute shared by all objects ===")
print("Total items created:", LibraryItem.total_items)

print("\n=== 6. Encapsulation ===")
try:
    print(book.__available)
except AttributeError as e:
    print("AttributeError:", e)
print("Using the method instead -> available?", book.is_available())
