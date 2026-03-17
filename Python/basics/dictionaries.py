"""
Python Dictionaries - Key-Value Pairs, Methods, and Nesting
"""

# 1. Creating Dictionaries
# Dictionaries are unordered mappings of key-value pairs.
# They use curly braces {} and colons to define key: value pairs.
# They are optimized for fast lookups by key (unlike lists which lookup by index).
print("--- Creating Dictionaries ---")
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Dictionary: {my_dict}")
print(f"Type: {type(my_dict)}")


# 2. Accessing Values
print("\n--- Accessing Values ---")
print(f"Name: {my_dict['name']}")

# Using .get() is safer (returns None instead of raising KeyError if key is missing)
print(f"Age (via .get()): {my_dict.get('age')}")
print(f"Missing key (via .get()): {my_dict.get('phone', 'Not Found')}")


# 3. Adding and Updating Items
print("\n--- Adding & Updating ---")
my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
print(f"After adding email: {my_dict}")

my_dict["age"] = 31  # Updating an existing key
print(f"After updating age: {my_dict}")


# 4. Removing Items
print("\n--- Removing Items ---")
del my_dict["email"]
print(f"After del 'email': {my_dict}")

popped_value = my_dict.pop("city")
print(f"After pop('city'): {my_dict}, popped value: {popped_value}")


# 5. Dictionary Methods
print("\n--- Dictionary Methods ---")
student = {"name": "Bob", "major": "CS", "gpa": 3.8}

print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items (key-value tuples): {list(student.items())}")

# Iterating through a dictionary
print("\nIterating:")
for key, value in student.items():
    print(f"  {key}: {value}")


# 6. Nested Dictionaries
print("\n--- Nested Dictionaries ---")
school = {
    "student_1": {"name": "Alice", "grade": "A"},
    "student_2": {"name": "Bob", "grade": "B+"},
}

print(f"Student 1 name: {school['student_1']['name']}")
print(f"Student 2 grade: {school['student_2']['grade']}")


# 7. Dictionary Comprehensions
print("\n--- Dictionary Comprehensions ---")
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares: {square_dict}")


# 8. Common Operations
print("\n--- Common Operations ---")
d = {"a": 1, "b": 2, "c": 3}
print(f"Length: {len(d)}")
print(f"Check key membership ('a' in d): {'a' in d}")
print(f"Check key membership ('z' in d): {'z' in d}")

# Merging dictionaries (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = d1 | d2
print(f"Merged (d1 | d2): {merged}")
