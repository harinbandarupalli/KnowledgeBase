"""
Python Functions - def, Arguments, Return Values, Logic, Tuple Unpacking, and Interactions
"""

# ============================================================
# 1. Introduction to Functions & the def Keyword
# ============================================================
# Functions are reusable blocks of code. Defined with the 'def' keyword.
print("--- Defining Functions ---")

def greet():
    """A simple function with no parameters."""
    print("  Hello from a function!")

greet()  # Calling the function
greet()  # Can be called multiple times


# ============================================================
# 2. Basics of Python Functions (Parameters & Return)
# ============================================================
print("\n--- Parameters and Return ---")

def add(a, b):
    """Takes two numbers and returns their sum."""
    return a + b

result = add(10, 20)
print(f"  add(10, 20) = {result}")


# Default Parameters
def greet_person(name, greeting="Hello"):
    """Greeting has a default value if not provided."""
    return f"{greeting}, {name}!"

print(f"  greet_person('Alice') = {greet_person('Alice')}")
print(f"  greet_person('Bob', 'Hey') = {greet_person('Bob', 'Hey')}")


# Keyword Arguments (order doesn't matter when using names)
print(f"  greet_person(greeting='Hi', name='Charlie') = {greet_person(greeting='Hi', name='Charlie')}")


# ============================================================
# 3. *args and **kwargs
# ============================================================
print("\n--- *args and **kwargs ---")

# *args allows a function to accept ANY number of positional arguments (as a tuple)
def sum_all(*args):
    """Sums any number of values."""
    print(f"  args = {args}, type = {type(args)}")
    return sum(args)

print(f"  sum_all(1,2,3) = {sum_all(1, 2, 3)}")
print(f"  sum_all(10,20,30,40) = {sum_all(10, 20, 30, 40)}")


# **kwargs allows a function to accept ANY number of keyword arguments (as a dict)
def print_info(**kwargs):
    """Prints any number of key=value pairs."""
    print(f"  kwargs = {kwargs}, type = {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"    {key}: {value}")

print_info(name="Alice", age=30, city="NYC")


# Combining regular, *args, and **kwargs
def combined(required, *args, **kwargs):
    print(f"  required={required}, args={args}, kwargs={kwargs}")

combined("hello", 1, 2, 3, x=10, y=20)


# ============================================================
# 4. Logic with Python Functions
# ============================================================
print("\n--- Logic in Functions ---")

def is_even(num):
    """Returns True if number is even."""
    return num % 2 == 0

print(f"  is_even(4) = {is_even(4)}")
print(f"  is_even(7) = {is_even(7)}")


def check_grade(score):
    """Returns a letter grade based on score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(f"  check_grade(85) = {check_grade(85)}")
print(f"  check_grade(42) = {check_grade(42)}")


# Early return pattern
def find_first_even(numbers):
    """Returns the first even number, or None."""
    for num in numbers:
        if num % 2 == 0:
            return num  # Exits immediately
    return None

print(f"  find_first_even([1,3,5,8,9]) = {find_first_even([1, 3, 5, 8, 9])}")
print(f"  find_first_even([1,3,5]) = {find_first_even([1, 3, 5])}")


# ============================================================
# 5. Tuple Unpacking with Functions
# ============================================================
print("\n--- Tuple Unpacking with Functions ---")

# Functions can return multiple values as a tuple
def get_stats(numbers):
    """Returns min, max, and average."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = [10, 20, 30, 40, 50]

# Unpacking the returned tuple directly
low, high, avg = get_stats(data)
print(f"  Data: {data}")
print(f"  Min={low}, Max={high}, Avg={avg}")

# You can also keep it as a tuple
stats = get_stats(data)
print(f"  As tuple: {stats}")


# Passing tuples/lists as arguments with *
def multiply(a, b, c):
    return a * b * c

values = (2, 3, 4)
print(f"  multiply(*{values}) = {multiply(*values)}")


# ============================================================
# 6. Interactions Between Functions
# ============================================================
print("\n--- Functions Calling Functions ---")

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def apply_operation(func, value):
    """Takes a function and a value, and applies the function."""
    return func(value)

print(f"  apply_operation(square, 5) = {apply_operation(square, 5)}")
print(f"  apply_operation(cube, 3) = {apply_operation(cube, 3)}")


# Building pipelines of functions
def clean_text(text):
    return text.strip()

def capitalize_text(text):
    return text.title()

def add_greeting(text):
    return f"Hello, {text}!"

# Chain functions together
raw = "   alice smith   "
result = add_greeting(capitalize_text(clean_text(raw)))
print(f"  Pipeline: '{raw}' -> '{result}'")


# Nested helper functions
def process_grades(grades):
    """Uses an inner helper function."""
    def letter_grade(score):
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        else: return "F"

    return {student: letter_grade(score) for student, score in grades.items()}

student_scores = {"Alice": 95, "Bob": 82, "Charlie": 68}
print(f"  Grades: {process_grades(student_scores)}")


# ============================================================
# 7. Type Hints (Modern Python)
# ============================================================
print("\n--- Type Hints ---")

def calculate_area(length: float, width: float) -> float:
    """Type hints document expected types (not enforced at runtime)."""
    return length * width

print(f"  calculate_area(5.0, 3.0) = {calculate_area(5.0, 3.0)}")
print("  Type hints help IDEs, linters (mypy), and other developers understand your code.")


# ============================================================
# 8. Docstrings
# ============================================================
print("\n--- Docstrings ---")

def complex_function(data: list[int], threshold: int = 10) -> list[int]:
    """
    Filters a list of integers to only include values above a threshold.

    Args:
        data: A list of integers to filter.
        threshold: The minimum value to include (default: 10).

    Returns:
        A new list containing only values greater than the threshold.
    """
    return [x for x in data if x > threshold]

print(f"  complex_function([5, 15, 25, 3, 42], 10) = {complex_function([5, 15, 25, 3, 42], 10)}")
print(f"  Docstring: {complex_function.__doc__[:60]}...")
