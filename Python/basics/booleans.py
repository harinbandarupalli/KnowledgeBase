"""
Python Booleans - True, False, and Comparison Operators
"""

# 1. Boolean Basics
# Booleans represent one of two values: True or False.
# They are the foundation of all conditional logic in Python.
print("--- Boolean Basics ---")
a = True
b = False
print(f"a = {a}, Type: {type(a)}")
print(f"b = {b}, Type: {type(b)}")

# Booleans are actually a subclass of integers (True=1, False=0)
print(f"True + True = {True + True}")   # 2
print(f"True * 10 = {True * 10}")       # 10
print(f"False + 5 = {False + 5}")       # 5


# 2. Comparison Operators (return Booleans)
print("\n--- Comparison Operators ---")
x = 10
y = 20

print(f"{x} == {y}: {x == y}")  # Equal to
print(f"{x} != {y}: {x != y}")  # Not equal to
print(f"{x} > {y}: {x > y}")    # Greater than
print(f"{x} < {y}: {x < y}")    # Less than
print(f"{x} >= {y}: {x >= y}")  # Greater than or equal to
print(f"{x} <= {y}: {x <= y}")  # Less than or equal to


# 3. Logical Operators (and, or, not)
print("\n--- Logical Operators ---")
print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"False or False: {False or False}")
print(f"not True: {not True}")
print(f"not False: {not False}")

# Combined example
age = 25
has_license = True
can_drive = age >= 16 and has_license
print(f"\nAge={age}, License={has_license} -> Can drive: {can_drive}")


# 4. Truthiness and Falsiness
# Python considers some values as "Truthy" (evaluate to True) and others as "Falsy" (evaluate to False)
print("\n--- Truthiness & Falsiness ---")
print("Falsy values (evaluate to False):")
falsy_values = [0, 0.0, "", [], {}, set(), None, False]
for val in falsy_values:
    print(f"  bool({val!r:10}) = {bool(val)}")

print("\nTruthy values (evaluate to True):")
truthy_values = [1, -1, 3.14, "hello", [1], {"a": 1}, {1, 2}, True]
for val in truthy_values:
    print(f"  bool({val!r:15}) = {bool(val)}")


# 5. Identity Operators (is, is not)
print("\n--- Identity Operators ---")
# `is` checks if two variables point to the SAME object in memory (not just equal values)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b (same value): {a == b}")         # True
print(f"a is b (same object): {a is b}")         # False - different objects
print(f"a is c (same object): {a is c}")         # True - c points to a

# `is` is commonly used with None
my_var = None
print(f"\nmy_var is None: {my_var is None}")
print(f"my_var is not None: {my_var is not None}")


# 6. Membership Operators (in, not in)
print("\n--- Membership Operators ---")
fruits = ["apple", "banana", "cherry"]
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")
