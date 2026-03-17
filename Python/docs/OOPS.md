# Object Oriented Programming (OOP) in Python

OOP allows you to create your own custom data types that bundle **data** (attributes) and **behavior** (methods) together. A **class** is the blueprint; an **object** is an instance built from it.

---

## Scripts

| # | Topic | File |
|---|-------|------|
| 1 | Classes, Attributes & Methods | [oop_classes_attributes.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/oop_classes_attributes.py) |
| 2 | Inheritance & Polymorphism | [oop_inheritance_polymorphism.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/oop_inheritance_polymorphism.py) |
| 3 | Special (Dunder) Methods | [oop_dunder_methods.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/oop_dunder_methods.py) |

---

## 1. Classes, Attributes & the `class` Keyword

```python
class Dog:
    species = "Canis familiaris"    # Class attribute (shared by ALL instances)

    def __init__(self, name, breed):
        self.name = name            # Instance attribute (unique per object)
        self.breed = breed

    def speak(self):                # Instance method
        return f"{self.name} says Woof!"

buddy = Dog("Buddy", "Golden Retriever")  # Creating an instance
```

### Key Concepts
- **`class` keyword** — defines a new type
- **`__init__`** — constructor, runs when you create an object
- **`self`** — refers to the specific instance (like `this` in Java/JS)
- **Class attributes** — shared across all instances
- **Instance attributes** — unique to each object
- **Instance methods** — functions that operate on an instance's data

---

## 2. Inheritance

A child class inherits all attributes and methods from a parent class, and can add or override them.

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        return f"{self.name} says {self.sound}!"

class Dog(Animal):                  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name, sound="Woof")  # Call parent's __init__
        self.breed = breed
    def fetch(self):                # New method only for Dog
        return f"{self.name} fetches!"
```

### Key Concepts
- **`super()`** — calls the parent class's methods
- **Method Overriding** — child redefines a parent method
- **`isinstance(obj, Class)`** — check if an object is of a certain type
- **`issubclass(Child, Parent)`** — check if one class inherits from another
- **Multiple Inheritance** — a class can inherit from multiple parents
- **MRO (Method Resolution Order)** — the order Python searches for methods

---

## 3. Polymorphism

Same method name, different behavior depending on the object's class.

```python
shapes = [Rectangle(4, 6), Circle(3)]
for shape in shapes:
    print(shape.area())   # Each class computes area differently
```

Any function that calls `.area()` works with ANY object that has that method — this is **polymorphism**.

---

## 4. Special (Magic/Dunder) Methods

Dunder methods let you define how your objects interact with Python's built-in operations.

| Dunder Method | Triggered By | Purpose |
|---|---|---|
| `__init__` | `MyClass()` | Constructor |
| `__str__` | `print(obj)`, `str(obj)` | User-friendly string |
| `__repr__` | `repr(obj)`, REPL | Developer-friendly string |
| `__len__` | `len(obj)` | Return length |
| `__getitem__` | `obj[i]` | Enable indexing |
| `__contains__` | `x in obj` | Enable membership check |
| `__eq__` | `obj1 == obj2` | Equality comparison |
| `__lt__`, `__gt__` | `<`, `>` | Ordering (enables `sorted()`) |
| `__add__` | `obj1 + obj2` | Addition operator |
| `__bool__` | `bool(obj)`, `if obj:` | Truthiness |

### Example: Making a Custom Object "Sortable"
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def __lt__(self, other):
        return self.celsius < other.celsius
    def __eq__(self, other):
        return self.celsius == other.celsius

temps = [Temperature(30), Temperature(10), Temperature(25)]
sorted(temps)  # Works because __lt__ is defined!
```

---

## Quick Reference: OOP Vocabulary

| Term | Definition |
|---|---|
| **Class** | A blueprint for creating objects |
| **Object / Instance** | A specific thing created from a class |
| **Attribute** | A variable that belongs to an object or class |
| **Method** | A function that belongs to an object |
| **Inheritance** | A child class gets all features of its parent |
| **Polymorphism** | Same interface, different behavior per class |
| **Encapsulation** | Bundling data and methods together; hiding internals |
| **Dunder Method** | Special `__method__` that hooks into Python operators |
