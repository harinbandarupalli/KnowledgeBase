"""
Python Errors and Exception Handling - try, except, finally, raise
"""

# ============================================================
# 1. Common Error Types
# ============================================================
print("--- Common Error Types ---")

errors = {
    "SyntaxError":      "Invalid Python syntax (caught before running)",
    "NameError":        "Using a variable that doesn't exist",
    "TypeError":        "Wrong type for an operation (e.g., '2' + 2)",
    "ValueError":       "Right type, wrong value (e.g., int('hello'))",
    "IndexError":       "List index out of range",
    "KeyError":         "Dictionary key doesn't exist",
    "AttributeError":   "Object has no such attribute/method",
    "FileNotFoundError":"Trying to open a file that doesn't exist",
    "ZeroDivisionError":"Dividing by zero",
    "ImportError":      "Failed to import a module",
    "IOError":          "Input/output operation failed",
    "OverflowError":    "Number too large for its type",
    "StopIteration":    "Iterator has no more items",
}
for err, desc in errors.items():
    print(f"  {err:22} -> {desc}")


# ============================================================
# 2. Basic try / except
# ============================================================
print("\n--- Basic try/except ---")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("  Caught: Can't divide by zero!")

try:
    num = int("hello")
except ValueError:
    print("  Caught: 'hello' is not a valid integer!")


# ============================================================
# 3. Catching Multiple Exceptions
# ============================================================
print("\n--- Multiple Exceptions ---")

# Method 1: Multiple except blocks
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("  Caught IndexError: index out of range")
except TypeError:
    print("  Caught TypeError")

# Method 2: Catch multiple in one line
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"  Caught: {type(e).__name__}: {e}")


# ============================================================
# 4. try / except / else / finally
# ============================================================
print("\n--- try/except/else/finally ---")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("  Error: division by zero")
else:
    # Runs ONLY if NO exception occurred
    print(f"  Success! Result = {result}")
finally:
    # ALWAYS runs, whether exception or not
    print("  Finally block: cleanup happens here (close files, connections, etc.)")


# ============================================================
# 5. Catching All Exceptions (use sparingly)
# ============================================================
print("\n--- Catching All Exceptions ---")

try:
    x = 1 / 0
except Exception as e:
    print(f"  Caught: {type(e).__name__}: {e}")
    # Use 'Exception' to catch all exceptions (except SystemExit, KeyboardInterrupt)

# AVOID bare 'except:' — it catches everything including Ctrl+C
# try:
#     ...
# except:            # BAD — catches KeyboardInterrupt too
#     pass


# ============================================================
# 6. Raising Exceptions
# ============================================================
print("\n--- Raising Exceptions ---")

def validate_age(age):
    """Raise an exception if age is invalid."""
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")
    if age > 150:
        raise ValueError(f"Age seems unrealistic, got {age}")
    return f"Age {age} is valid"

try:
    print(f"  {validate_age(25)}")
    print(f"  {validate_age(-5)}")
except ValueError as e:
    print(f"  Caught ValueError: {e}")

try:
    validate_age("twenty")
except TypeError as e:
    print(f"  Caught TypeError: {e}")


# ============================================================
# 7. Custom Exceptions
# ============================================================
print("\n--- Custom Exceptions ---")

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount}. Balance is only ${balance}."
        )

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(100)
try:
    account.withdraw(50)
    print(f"  After $50 withdrawal: ${account.balance}")
    account.withdraw(200)
except InsufficientFundsError as e:
    print(f"  Caught: {e}")


# ============================================================
# 8. Exception Chaining (raise from)
# ============================================================
print("\n--- Exception Chaining ---")

def load_config(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError as e:
        # Chain the original exception for debugging
        raise RuntimeError(f"Failed to load config: {filename}") from e

try:
    load_config("nonexistent_config.yaml")
except RuntimeError as e:
    print(f"  Caught: {e}")
    print(f"  Caused by: {e.__cause__}")


# ============================================================
# 9. Context Managers and Exceptions
# ============================================================
print("\n--- Context Managers ---")
print("  'with' statements automatically handle cleanup on exceptions:")
print("    with open('file.txt') as f:    # File is auto-closed even if error occurs")
print("        data = f.read()")
print()
print("  Custom context managers can be created with __enter__/__exit__ or @contextmanager")


# ============================================================
# 10. Best Practices
# ============================================================
print("\n--- Best Practices ---")
practices = [
    "Catch SPECIFIC exceptions, not bare 'except:'",
    "Use 'else' for code that should only run on success",
    "Use 'finally' for cleanup (closing files, connections)",
    "Don't use exceptions for flow control (use if/else instead)",
    "Create custom exceptions for domain-specific errors",
    "Log exceptions in production code",
    "Re-raise with 'raise' or chain with 'raise ... from ...'",
    "Keep try blocks as small as possible",
]
for i, p in enumerate(practices, 1):
    print(f"  {i}. {p}")
