"""
Object Oriented Programming - Special (Magic/Dunder) Methods
"""

# Dunder methods (double underscore) allow you to define how your objects
# behave with built-in Python operations like print(), len(), +, ==, etc.

# ============================================================
# 1. __init__ and __str__ and __repr__
# ============================================================
print("--- __init__, __str__, __repr__ ---")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Called by print() and str(). User-friendly output."""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """Called in the REPL and by repr(). Developer-friendly output."""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

book = Book("Python Crash Course", "Eric Matthes", 544)
print(f"  str:  {book}")        # Calls __str__
print(f"  repr: {repr(book)}")  # Calls __repr__


# ============================================================
# 2. __len__
# ============================================================
print("\n--- __len__ ---")

class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"

playlist = Playlist("Chill Vibes", ["Song A", "Song B", "Song C"])
print(f"  {playlist}")
print(f"  len(playlist) = {len(playlist)}")


# ============================================================
# 3. __getitem__ — Makes object subscriptable (indexable)
# ============================================================
print("\n--- __getitem__ ---")

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = [f"{r} of {s}" for s in self.suits for r in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

deck = Deck()
print(f"  Total cards: {len(deck)}")
print(f"  First card: {deck[0]}")
print(f"  Last card: {deck[-1]}")
print(f"  Slice [0:3]: {deck[0:3]}")


# ============================================================
# 4. Comparison Dunder Methods
# ============================================================
print("\n--- __eq__, __lt__, __gt__ ---")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __gt__(self, other):
        return self.celsius > other.celsius

    def __le__(self, other):
        return self.celsius <= other.celsius

    def __str__(self):
        return f"{self.celsius}°C"

t1 = Temperature(20)
t2 = Temperature(30)
t3 = Temperature(20)

print(f"  {t1} == {t3}: {t1 == t3}")
print(f"  {t1} < {t2}: {t1 < t2}")
print(f"  {t2} > {t1}: {t2 > t1}")

# Now sorting works automatically!
temps = [Temperature(30), Temperature(10), Temperature(25)]
sorted_temps = sorted(temps)
print(f"  Sorted: {[str(t) for t in sorted_temps]}")


# ============================================================
# 5. Arithmetic Dunder Methods
# ============================================================
print("\n--- __add__, __sub__, __mul__ ---")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"  {v1} + {v2} = {v1 + v2}")
print(f"  {v1} - {v2} = {v1 - v2}")
print(f"  {v1} * 3 = {v1 * 3}")
print(f"  abs({v1}) = {abs(v1)}")  # Magnitude


# ============================================================
# 6. __contains__ — Enables the 'in' keyword
# ============================================================
print("\n--- __contains__ ---")

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __contains__(self, person):
        return person in self.members

    def __str__(self):
        return f"Team {self.name}: {self.members}"

team = Team("Alpha", ["Alice", "Bob", "Charlie"])
print(f"  {team}")
print(f"  'Alice' in team: {'Alice' in team}")
print(f"  'Dave' in team: {'Dave' in team}")


# ============================================================
# 7. __bool__ — Controls truthiness
# ============================================================
print("\n--- __bool__ ---")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __bool__(self):
        return len(self.items) > 0

    def __len__(self):
        return len(self.items)

cart = ShoppingCart()
print(f"  Empty cart is truthy: {bool(cart)}")
cart.add("Laptop")
print(f"  Cart with items is truthy: {bool(cart)}")


# ============================================================
# Summary of Common Dunder Methods
# ============================================================
print("\n--- Common Dunder Methods Summary ---")
dunders = {
    "__init__":     "Constructor — called when creating an instance",
    "__str__":      "Called by print() and str() — user-friendly",
    "__repr__":     "Called by repr() and in REPL — developer-friendly",
    "__len__":      "Called by len()",
    "__getitem__":  "Called by obj[index] — makes object indexable",
    "__contains__": "Called by 'in' keyword",
    "__eq__":       "Called by == operator",
    "__lt__/__gt__":"Called by < and > operators",
    "__add__":      "Called by + operator",
    "__sub__":      "Called by - operator",
    "__mul__":      "Called by * operator",
    "__bool__":     "Called by bool() — controls truthiness",
    "__abs__":      "Called by abs()",
    "__del__":      "Destructor — called when object is garbage collected",
}
for method, desc in dunders.items():
    print(f"  {method:16} -> {desc}")
