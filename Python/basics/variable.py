"""
Python Variables - Assignment and Dynamic Typing
"""

# 1. Variable Assignment
# Python determines the type automatically based on the value assigned.
# Variable names should be lowercase, with words separated by underscores (snake_case).
my_name = "Alice"
my_age = 30
is_student = True

print(f"Name: {my_name}, Age: {my_age}, Student: {is_student}")

# 2. Reassignment and Dynamic Typing
# Python is "dynamically typed", meaning a variable can change its data type if reassigned.
print("\n--- Dynamic Typing ---")
my_variable = 100
print(f"Current Value: {my_variable}, Type: {type(my_variable)}")

# Reassigning to a string (perfectly valid in Python)
my_variable = "Now I am a string!"
print(f"Current Value: {my_variable}, Type: {type(my_variable)}")

# Reassigning to a list
my_variable = [1, 2, 3]
print(f"Current Value: {my_variable}, Type: {type(my_variable)}")


# 3. Multiple Assignment
print("\n--- Multiple Assignment ---")
# You can assign values to multiple variables in one line.
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# You can also assign the same value to multiple variables.
a = b = c = 10
print(f"a={a}, b={b}, c={c}")


# 4. Using Variables in Expressions
print("\n--- Expressions with Variables ---")
income = 50000
tax_rate = 0.2
taxes_owed = income * tax_rate
net_income = income - taxes_owed

print(f"Income: ${income}")
print(f"Taxes Owed: ${taxes_owed}")
print(f"Net Income: ${net_income}")


# 5. Variable Naming Rules
# - Can contain letters, numbers, and underscores
# - Cannot start with a number (e.g., 1invalid_name)
# - Cannot contain spaces
# - Cannot use reserved keywords (e.g., class, for, if, def)
# - Python is case-sensitive (my_var is different from My_Var)

valid_name_123 = "Valid"
_private_variable = "Prefixed with underscore marks it as 'private' by convention"
