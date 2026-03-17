"""
Python List Comprehensions - Concise Ways to Create and Transform Lists
"""

# 1. Basic List Comprehension
# Syntax: [expression for item in iterable]
print("--- Basic List Comprehension ---")
squares = [x ** 2 for x in range(1, 11)]
print(f"Squares of 1-10: {squares}")

# Equivalent long-form:
squares_long = []
for x in range(1, 11):
    squares_long.append(x ** 2)
# squares == squares_long


# 2. List Comprehension with Condition (Filter)
# Syntax: [expression for item in iterable if condition]
print("\n--- With Condition (Filter) ---")
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers 1-20: {evens}")

long_words = [word for word in ["hi", "hello", "hey", "howdy", "yo"] if len(word) > 2]
print(f"Words longer than 2 chars: {long_words}")


# 3. List Comprehension with if/else (Transform)
# Syntax: [value_if_true if condition else value_if_false for item in iterable]
# NOTE: When using if/else, the condition goes BEFORE 'for' (not after).
print("\n--- With if/else (Transform) ---")
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 11)]
print(f"Even/Odd labels: {labels}")

capped = [min(x, 50) for x in [10, 30, 50, 70, 90]]
print(f"Capped at 50: {capped}")


# 4. Nested List Comprehensions
print("\n--- Nested Comprehensions ---")
# Flatten a 2D list into a 1D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(f"Flattened matrix: {flat}")

# Create a multiplication table
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Multiplication table:")
for row in table:
    print(f"  {row}")


# 5. String Operations with Comprehensions
print("\n--- String Comprehensions ---")
sentence = "Hello World Python"
first_letters = [word[0] for word in sentence.split()]
print(f"First letters: {first_letters}")

cleaned = [char.lower() for char in "Hello, World! 123" if char.isalpha()]
print(f"Only lowercase letters: {''.join(cleaned)}")


# 6. Dictionary Comprehensions
# Syntax: {key_expr: value_expr for item in iterable}
print("\n--- Dictionary Comprehensions ---")
square_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Square dict: {square_dict}")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")


# 7. Set Comprehensions
# Syntax: {expression for item in iterable}
print("\n--- Set Comprehensions ---")
unique_lengths = {len(word) for word in ["hello", "world", "hi", "hey", "howdy"]}
print(f"Unique word lengths: {unique_lengths}")


# 8. Generator Expressions (Memory-Efficient)
# Syntax: (expression for item in iterable)
# Generators don't store all values in memory — they yield one at a time.
print("\n--- Generator Expressions ---")
gen = (x ** 2 for x in range(1, 6))
print(f"Generator object: {gen}")
print(f"Converted to list: {list(gen)}")

# Great for large data — compute sum without storing the entire list
total = sum(x ** 2 for x in range(1, 1001))
print(f"Sum of squares 1-1000: {total}")


# 9. When NOT to Use Comprehensions
print("\n--- When NOT to Use Comprehensions ---")
print("Avoid comprehensions when:")
print("  - The logic is complex (use a regular for loop for readability)")
print("  - You need side effects (e.g., printing, writing to files)")
print("  - The expression spans multiple lines (hard to read)")
print("Rule of thumb: If it doesn't fit in one readable line, use a regular loop.")
