"""
Object Oriented Programming - Inheritance and Polymorphism
"""

# ============================================================
# 1. Inheritance — A class can inherit from another class
# ============================================================
print("--- Basic Inheritance ---")

class Animal:
    """Base (Parent) class."""
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def info(self):
        return f"Animal(name={self.name})"


class Dog(Animal):
    """Child class — inherits from Animal."""
    def __init__(self, name, breed):
        # Call the parent's __init__ using super()
        super().__init__(name, sound="Woof")
        self.breed = breed  # New attribute specific to Dog

    def fetch(self):
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    """Another child class."""
    def __init__(self, name, indoor=True):
        super().__init__(name, sound="Meow")
        self.indoor = indoor


dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(f"  {dog.speak()}")       # Inherited method
print(f"  {dog.fetch()}")       # Dog-specific method
print(f"  Breed: {dog.breed}")
print(f"  {cat.speak()}")
print(f"  Indoor: {cat.indoor}")


# ============================================================
# 2. Method Overriding — Child redefines a parent method
# ============================================================
print("\n--- Method Overriding ---")

class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"{self.__class__.__name__}: area = {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # Overrides Shape.area()
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Overrides Shape.area()
        return 3.14159 * self.radius ** 2


rect = Rectangle(10, 5)
circ = Circle(7)

print(f"  {rect.describe()}")
print(f"  {circ.describe()}")


# ============================================================
# 3. Polymorphism — Same interface, different behavior
# ============================================================
print("\n--- Polymorphism ---")

# All shapes have .area() and .describe(), but each computes it differently.
# This is polymorphism — same method name, different implementations.

shapes = [Rectangle(4, 6), Circle(3), Rectangle(2, 8)]

for shape in shapes:
    print(f"  {shape.describe()}")  # Python calls the correct .area() for each type


# Polymorphism with functions
def print_area(shape):
    """Works with ANY object that has an .area() method."""
    print(f"  Area of {shape.__class__.__name__}: {shape.area():.2f}")

print_area(Rectangle(5, 5))
print_area(Circle(10))


# ============================================================
# 4. isinstance() and issubclass()
# ============================================================
print("\n--- isinstance() and issubclass() ---")
print(f"  isinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"  isinstance(dog, Animal): {isinstance(dog, Animal)}")  # Dog IS an Animal
print(f"  isinstance(cat, Dog): {isinstance(cat, Dog)}")

print(f"  issubclass(Dog, Animal): {issubclass(Dog, Animal)}")
print(f"  issubclass(Animal, Dog): {issubclass(Animal, Dog)}")


# ============================================================
# 5. Multiple Inheritance
# ============================================================
print("\n--- Multiple Inheritance ---")

class Flyer:
    def fly(self):
        return f"{self.__class__.__name__} can fly!"

class Swimmer:
    def swim(self):
        return f"{self.__class__.__name__} can swim!"

class Duck(Animal, Flyer, Swimmer):
    def __init__(self, name):
        super().__init__(name, sound="Quack")

donald = Duck("Donald")
print(f"  {donald.speak()}")
print(f"  {donald.fly()}")
print(f"  {donald.swim()}")

# Method Resolution Order (MRO) — the order Python searches for methods
print(f"  MRO: {[cls.__name__ for cls in Duck.__mro__]}")
