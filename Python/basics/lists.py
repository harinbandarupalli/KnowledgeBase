"""
Python Lists - Creating, Indexing, Slicing, and Methods
"""

# 1. Creating Lists
# Lists are ordered, mutable sequences that can hold any data type.
print("--- Creating Lists ---")
my_list = [1, 2, 3]
mixed_list = [1, "Hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]

print(f"Simple List: {my_list}")
print(f"Mixed Types: {mixed_list}")
print(f"Nested List: {nested_list}")
print(f"Length of my_list: {len(my_list)}")


# 2. Indexing and Slicing (works like strings)
print("\n--- Indexing & Slicing ---")
letters = ["a", "b", "c", "d", "e"]

print(f"First element [0]: {letters[0]}")
print(f"Last element [-1]: {letters[-1]}")
print(f"Slice [1:4]: {letters[1:4]}")  # ['b', 'c', 'd']
print(f"Reverse [::-1]: {letters[::-1]}")

# Nested list indexing
print(f"Nested list [1][0]: {nested_list[1][0]}")  # 3


# 3. Mutability - Lists CAN be changed (unlike strings)
print("\n--- Mutability ---")
colors = ["red", "green", "blue"]
colors[0] = "yellow"
print(f"After reassigning index 0: {colors}")


# 4. List Methods
print("\n--- List Methods ---")
nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Appending items
nums.append(10)
print(f"After append(10): {nums}")

# Inserting at a specific index
nums.insert(0, 99)
print(f"After insert(0, 99): {nums}")

# Removing items
nums.remove(99)  # Removes the FIRST occurrence of the value
print(f"After remove(99): {nums}")

popped_item = nums.pop()  # Removes and returns the LAST item
print(f"After pop(): {nums}, popped item was: {popped_item}")

popped_at_index = nums.pop(0)  # Removes and returns item at specific index
print(f"After pop(0): {nums}, popped item was: {popped_at_index}")

# Sorting
nums.sort()
print(f"After sort(): {nums}")

nums.reverse()
print(f"After reverse(): {nums}")

# Extending a list with another list
nums.extend([100, 200])
print(f"After extend([100, 200]): {nums}")

# Count occurrences
print(f"Count of 1: {nums.count(1)}")

# Find index
print(f"Index of 5: {nums.index(5)}")


# 5. List Comprehensions (Pythonic way to create lists)
print("\n--- List Comprehensions ---")
squares = [x**2 for x in range(1, 11)]
print(f"Squares of 1-10: {squares}")

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers 1-20: {even_numbers}")


# 6. Common Operations
print("\n--- Common Operations ---")
nums = [10, 20, 30, 40, 50]
print(f"Min: {min(nums)}")
print(f"Max: {max(nums)}")
print(f"Sum: {sum(nums)}")
print(f"Check membership (20 in nums): {20 in nums}")

# Concatenation
list_a = [1, 2]
list_b = [3, 4]
combined = list_a + list_b
print(f"Concatenated: {combined}")

# Repetition
repeated = [0] * 5
print(f"Repeated: {repeated}")
