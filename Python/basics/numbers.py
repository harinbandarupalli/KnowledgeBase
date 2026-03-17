"""
Python Numbers - Basics and Arithmetic Operations
"""

# 1. Basic Types of Numbers
# Integers (Whole numbers)
my_int = 100
print(f"Integer: {my_int} (Type: {type(my_int)})")

# Floating Point Numbers (Numbers with decimals)
my_float = 3.14159
print(f"Float: {my_float} (Type: {type(my_float)})")


# 2. Basic Arithmetic Operations
print("\n--- Basic Arithmetic ---")
a = 15
b = 4

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")

# True Division (always returns a float)
print(f"Division: {a} / {b} = {a / b}")

# Floor Division (truncates the decimal to return an integer)
print(f"Floor Division: {a} // {b} = {a // b}")

# Modulo (returns the remainder of the division)
print(f"Modulo (Remainder): {a} % {b} = {a % b}")

# Exponentiation (Power)
print(f"Exponentiation: {a} ** 2 = {a ** 2}")


# 3. Order of Operations (PEMDAS)
print("\n--- Order of Operations ---")
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
calculation = 10 + 10 * 2
print(f"10 + 10 * 2 = {calculation}") # Multiplication happens first

calculation_with_parens = (10 + 10) * 2
print(f"(10 + 10) * 2 = {calculation_with_parens}") # Parentheses happen first


# 4. built-in number functions
print("\n--- Built-in Number Functions ---")
print(f"Absolute Value of -5: {abs(-5)}")
print(f"Rounding 3.14159 to 2 decimal places: {round(3.14159, 2)}")
print(f"Rounding 5.6 to nearest integer: {round(5.6)}")
