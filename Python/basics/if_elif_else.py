"""
Python If, Elif, and Else Statements - Control Flow
"""

# 1. Basic if Statement
# Executes a block of code only if the condition is True.
print("--- Basic if ---")
age = 20

if age >= 18:
    print(f"Age is {age}. You are an adult.")


# 2. if / else
# Provides an alternative block if the condition is False.
print("\n--- if / else ---")
temperature = 35

if temperature > 30:
    print(f"It's {temperature}°C — it's hot outside!")
else:
    print(f"It's {temperature}°C — the weather is fine.")


# 3. if / elif / else
# Chain multiple conditions. Python checks them top to bottom and runs the FIRST one that is True.
print("\n--- if / elif / else ---")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")


# 4. Nested if Statements
print("\n--- Nested if ---")
is_logged_in = True
is_admin = False

if is_logged_in:
    print("User is logged in.")
    if is_admin:
        print("  Welcome, Admin!")
    else:
        print("  Welcome, regular user.")
else:
    print("Please log in.")


# 5. Combining Conditions with Logical Operators
print("\n--- Logical Operators in Conditions ---")
x = 15

if x > 10 and x < 20:
    print(f"{x} is between 10 and 20")

if x < 5 or x > 10:
    print(f"{x} is outside the range 5-10")

if not (x == 100):
    print(f"{x} is not 100")


# 6. Ternary Operator (One-Line if/else)
# Syntax: value_if_true if condition else value_if_false
print("\n--- Ternary Operator ---")
age = 17
status = "adult" if age >= 18 else "minor"
print(f"Age {age} -> Status: {status}")

# Can be used inline
print(f"Can vote: {'Yes' if age >= 18 else 'No'}")


# 7. Truthiness in Conditions
# Python evaluates non-boolean values as True or False in conditions.
print("\n--- Truthiness in Conditions ---")
my_list = [1, 2, 3]

if my_list:  # Non-empty list is Truthy
    print(f"List has {len(my_list)} items")

empty_string = ""
if not empty_string:  # Empty string is Falsy
    print("String is empty")

value = None
if value is None:
    print("Value is None — use 'is None' instead of '== None'")


# 8. Match Statement (Python 3.10+ — Structural Pattern Matching)
print("\n--- Match Statement (Python 3.10+) ---")
http_status = 404

match http_status:
    case 200:
        print("OK")
    case 301:
        print("Moved Permanently")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print(f"Unknown status: {http_status}")
