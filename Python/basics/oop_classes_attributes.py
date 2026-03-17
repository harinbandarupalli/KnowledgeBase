"""
Object Oriented Programming - Introduction, the Class Keyword, and Attributes
"""

# ============================================================
# 1. What is OOP?
# ============================================================
# OOP allows you to create your own custom data types (classes) that bundle
# data (attributes) and behavior (methods) together.
# Think of a class as a BLUEPRINT and an object as an INSTANCE built from that blueprint.

print("--- Creating a Basic Class ---")

class Dog:
    """A simple Dog class."""

    # CLASS ATTRIBUTE — shared by ALL instances of Dog
    species = "Canis familiaris"

    # CONSTRUCTOR (__init__) — runs automatically when you create a new Dog
    def __init__(self, name, breed, age):
        # INSTANCE ATTRIBUTES — unique to each Dog object
        self.name = name
        self.breed = breed
        self.age = age

# Creating instances (objects) from the class
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "German Shepherd", 5)

print(f"  dog1: {dog1.name}, {dog1.breed}, Age {dog1.age}")
print(f"  dog2: {dog2.name}, {dog2.breed}, Age {dog2.age}")

# Class attribute is shared
print(f"  dog1.species: {dog1.species}")
print(f"  dog2.species: {dog2.species}")
print(f"  Dog.species:  {Dog.species}")


# ============================================================
# 2. Class vs Instance Attributes
# ============================================================
print("\n--- Class vs Instance Attributes ---")

class Counter:
    # Class attribute — shared across all instances
    total_count = 0

    def __init__(self, name):
        self.name = name          # Instance attribute
        Counter.total_count += 1  # Modifying the class attribute

c1 = Counter("A")
c2 = Counter("B")
c3 = Counter("C")

print(f"  Counter.total_count = {Counter.total_count}")  # 3
print(f"  c1.name = {c1.name}")  # Each has their own name


# ============================================================
# 3. Instance Methods
# ============================================================
print("\n--- Instance Methods ---")

class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area. 'self' refers to the specific instance."""
        return Circle.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * Circle.pi * self.radius

    def describe(self):
        return f"Circle(radius={self.radius}, area={self.area():.2f})"

c = Circle(5)
print(f"  {c.describe()}")
print(f"  Circumference: {c.circumference():.2f}")


# ============================================================
# 4. Modifying Attributes
# ============================================================
print("\n--- Modifying Attributes ---")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"  Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"  Insufficient funds! Balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"  Withdrew ${amount}. New balance: ${self.balance}")

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
