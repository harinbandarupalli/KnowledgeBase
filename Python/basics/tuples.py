"""
Python Tuples - Immutable Ordered Sequences
"""

# 1. Creating Tuples
# Tuples are like lists, but they are IMMUTABLE (cannot be changed after creation).
# They use parentheses () instead of square brackets [].
print("--- Creating Tuples ---")
my_tuple = (1, 2, 3)
mixed_tuple = (1, "Hello", 3.14)
single_element_tuple = (42,)  # NOTE: The trailing comma is required for single-element tuples!

print(f"Tuple: {my_tuple}")
print(f"Mixed Tuple: {mixed_tuple}")
print(f"Single Element: {single_element_tuple}, Type: {type(single_element_tuple)}")
print(f"Without comma: {type((42))}")  # This is just an int, NOT a tuple!


# 2. Indexing and Slicing (same as lists)
print("\n--- Indexing & Slicing ---")
t = ("a", "b", "c", "d", "e")

print(f"First element [0]: {t[0]}")
print(f"Last element [-1]: {t[-1]}")
print(f"Slice [1:4]: {t[1:4]}")


# 3. Immutability
print("\n--- Immutability ---")
# t[0] = "z"  # THIS WILL THROW A TypeError!
# Uncomment the line above to see the error.
print("Tuples cannot be modified after creation. This is their key feature.")
print("This makes them useful as dictionary keys and for data integrity.")


# 4. Tuple Methods
print("\n--- Tuple Methods ---")
t = (1, 2, 3, 2, 2, 4, 5)
print(f"Count of 2: {t.count(2)}")
print(f"Index of first 2: {t.index(2)}")


# 5. Tuple Unpacking
# A very common and powerful Python pattern.
print("\n--- Tuple Unpacking ---")
coordinates = (12.5, 45.8)
x, y = coordinates
print(f"x = {x}, y = {y}")

# Unpacking with * (star expression) to capture multiple values
first, *middle, last = (1, 2, 3, 4, 5)
print(f"First: {first}, Middle: {middle}, Last: {last}")


# 6. When to use Tuples vs Lists
print("\n--- Tuples vs Lists ---")
print("Use Tuples when:")
print("  - Data should NOT change (e.g., days of the week, coordinates)")
print("  - You need a hashable type (e.g., as dictionary keys)")
print("  - You want to signal to other developers that this data is constant")
print("Use Lists when:")
print("  - Data needs to be modified (append, remove, sort)")
print("  - You are building a collection of similar items")


# 7. Common Operations
print("\n--- Common Operations ---")
t = (10, 20, 30, 40, 50)
print(f"Length: {len(t)}")
print(f"Min: {min(t)}")
print(f"Max: {max(t)}")
print(f"Sum: {sum(t)}")
print(f"Membership (20 in t): {20 in t}")

# Converting between lists and tuples
my_list = [1, 2, 3]
converted_tuple = tuple(my_list)
back_to_list = list(converted_tuple)
print(f"List to Tuple: {converted_tuple}")
print(f"Tuple to List: {back_to_list}")
