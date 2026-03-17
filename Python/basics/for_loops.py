"""
Python For Loops - Iterating Over Sequences
"""

# 1. Basic For Loop
# Iterates over each item in a sequence (list, string, tuple, set, dict, range).
print("--- Basic For Loop ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  {fruit}")


# 2. Looping Through Strings
print("\n--- Looping Through a String ---")
for char in "Python":
    print(f"  {char}")


# 3. Using range()
# range(stop)          -> 0, 1, 2, ..., stop-1
# range(start, stop)   -> start, start+1, ..., stop-1
# range(start, stop, step) -> start, start+step, start+2*step, ...
print("\n--- range() ---")
print("range(5):", list(range(5)))
print("range(2, 8):", list(range(2, 8)))
print("range(0, 20, 3):", list(range(0, 20, 3)))
print("range(10, 0, -2):", list(range(10, 0, -2)))   # Countdown

for i in range(5):
    print(f"  Iteration {i}")


# 4. enumerate() - Get Index and Value
print("\n--- enumerate() ---")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"  Index {index}: {color}")

# Start from a custom number
for index, color in enumerate(colors, start=1):
    print(f"  Item #{index}: {color}")


# 5. zip() - Loop Over Multiple Lists Simultaneously
print("\n--- zip() ---")
names = ["Alice", "Bob", "Charlie"]
scores = [95, 82, 78]

for name, score in zip(names, scores):
    print(f"  {name}: {score}")


# 6. Nested For Loops
print("\n--- Nested For Loops ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  ({i}, {j})", end="")
    print()  # New line after inner loop


# 7. Loop with else
# The else block runs ONLY if the loop completes without hitting a 'break'.
print("\n--- For...Else ---")
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} was NOT found in the list.")


# 8. break and continue
print("\n--- break ---")
for i in range(10):
    if i == 5:
        print(f"  Breaking at {i}")
        break
    print(f"  {i}")

print("\n--- continue ---")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}")  # Only prints odd numbers


# 9. Looping Through Dictionaries
print("\n--- Looping Through Dictionaries ---")
student = {"name": "Alice", "major": "CS", "gpa": 3.8}

print("Keys:")
for key in student:
    print(f"  {key}")

print("Values:")
for value in student.values():
    print(f"  {value}")

print("Key-Value Pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")


# 10. Unpacking in Loops
print("\n--- Unpacking in Loops ---")
pairs = [(1, "one"), (2, "two"), (3, "three")]
for number, word in pairs:
    print(f"  {number} = {word}")
