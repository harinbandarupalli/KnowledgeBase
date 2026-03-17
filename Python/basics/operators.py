"""
Python Useful Operators - range, enumerate, zip, in, min, max, map, filter, lambda, and more
"""

# 1. range()
print("--- range() ---")
print(f"range(5): {list(range(5))}")
print(f"range(3, 10): {list(range(3, 10))}")
print(f"range(0, 20, 4): {list(range(0, 20, 4))}")


# 2. enumerate()
print("\n--- enumerate() ---")
words = ["hello", "world", "python"]
for index, word in enumerate(words, start=1):
    print(f"  {index}. {word}")


# 3. zip()
print("\n--- zip() ---")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"  {name}, age {age}, from {city}")

# Unzipping
zipped = list(zip(names, ages))
unzipped_names, unzipped_ages = zip(*zipped)
print(f"  Unzipped names: {unzipped_names}")


# 4. in Operator (Membership)
print("\n--- in Operator ---")
print(f"'a' in 'apple': {'a' in 'apple'}")
print(f"5 in [1, 2, 3]: {5 in [1, 2, 3]}")
print(f"'key' in {{'key': 1}}: {'key' in {'key': 1}}")


# 5. min, max, sum, abs, round
print("\n--- min, max, sum, abs, round ---")
nums = [45, 12, 89, 3, 67]
print(f"min: {min(nums)}")
print(f"max: {max(nums)}")
print(f"sum: {sum(nums)}")
print(f"abs(-42): {abs(-42)}")
print(f"round(3.14159, 2): {round(3.14159, 2)}")

# min/max with key function
words = ["banana", "apple", "cherry", "date"]
print(f"Shortest word: {min(words, key=len)}")
print(f"Longest word: {max(words, key=len)}")


# 6. sorted() and reversed()
print("\n--- sorted() and reversed() ---")
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"sorted(): {sorted(nums)}")
print(f"sorted(reverse=True): {sorted(nums, reverse=True)}")
print(f"reversed(): {list(reversed(nums))}")

# Sorting with a key
students = [("Alice", 88), ("Bob", 95), ("Charlie", 72)]
by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(f"Sorted by score: {by_score}")


# 7. lambda Functions (Anonymous Functions)
print("\n--- lambda ---")
# lambda arguments: expression
square = lambda x: x ** 2
print(f"square(5): {square(5)}")

add = lambda a, b: a + b
print(f"add(3, 7): {add(3, 7)}")


# 8. map() - Apply a Function to Every Item
print("\n--- map() ---")
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(f"Squares: {squared}")

# Convert list of strings to integers
str_nums = ["1", "2", "3", "4"]
int_nums = list(map(int, str_nums))
print(f"Converted: {int_nums}")


# 9. filter() - Keep Items That Match a Condition
print("\n--- filter() ---")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Even numbers: {evens}")


# 10. any() and all()
print("\n--- any() and all() ---")
bools = [True, False, True]
print(f"any([True, False, True]): {any(bools)}")  # At least one True?
print(f"all([True, False, True]): {all(bools)}")  # ALL True?

nums = [2, 4, 6, 8]
print(f"All even? {all(n % 2 == 0 for n in nums)}")
print(f"Any > 5? {any(n > 5 for n in nums)}")


# 11. Walrus Operator := (Python 3.8+)
print("\n--- Walrus Operator := ---")
# Assigns a value to a variable as part of an expression.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if (n := len(data)) > 5:
    print(f"List is long ({n} elements)")


# 12. Unpacking Operators (* and **)
print("\n--- Unpacking ---")
# * unpacks iterables
first, *rest = [1, 2, 3, 4, 5]
print(f"first={first}, rest={rest}")

# ** unpacks dictionaries
defaults = {"color": "blue", "size": 10}
overrides = {"size": 20, "weight": 5}
merged = {**defaults, **overrides}
print(f"Merged dict: {merged}")
