"""
Python Sets - Unordered Collections of Unique Elements
"""

# 1. Creating Sets
# Sets are unordered collections with NO duplicate elements.
# They use curly braces {} like dictionaries, but contain single values (not key:value pairs).
print("--- Creating Sets ---")
my_set = {1, 2, 3, 4, 5}
print(f"Set: {my_set}")

# Duplicates are automatically removed
duplicate_set = {1, 1, 2, 2, 3, 3}
print(f"Set with duplicates removed: {duplicate_set}")

# Creating a set from a list (great for removing duplicates!)
my_list = [1, 2, 2, 3, 3, 3, 4]
unique_items = set(my_list)
print(f"Unique items from list: {unique_items}")

# Empty set must be created with set(), NOT {} (that creates an empty dict)
empty_set = set()
print(f"Empty set: {empty_set}, Type: {type(empty_set)}")


# 2. Adding and Removing Elements
print("\n--- Adding & Removing ---")
s = {1, 2, 3}

s.add(4)
print(f"After add(4): {s}")

s.add(4)  # Adding a duplicate does nothing
print(f"After add(4) again: {s}")

s.discard(2)  # Removes element, does NOT raise error if missing
print(f"After discard(2): {s}")

s.remove(3)  # Removes element, RAISES KeyError if missing
print(f"After remove(3): {s}")

# s.remove(99)  # Uncomment to see KeyError


# 3. Set Operations (Mathematical)
print("\n--- Set Operations ---")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union: All elements from both sets
print(f"Union (A | B): {set_a | set_b}")
print(f"Union (method): {set_a.union(set_b)}")

# Intersection: Elements common to both sets
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Intersection (method): {set_a.intersection(set_b)}")

# Difference: Elements in A but NOT in B
print(f"Difference (A - B): {set_a - set_b}")
print(f"Difference (method): {set_a.difference(set_b)}")

# Symmetric Difference: Elements in A or B, but NOT both
print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}")
print(f"Symmetric Difference (method): {set_a.symmetric_difference(set_b)}")


# 4. Subset and Superset Checks
print("\n--- Subset & Superset ---")
small = {1, 2}
big = {1, 2, 3, 4, 5}

print(f"Is {small} a subset of {big}? {small.issubset(big)}")
print(f"Is {big} a superset of {small}? {big.issuperset(small)}")
print(f"Are {small} and {{6, 7}} disjoint (no common elements)? {small.isdisjoint({6, 7})}")


# 5. Frozen Sets (Immutable Sets)
print("\n--- Frozen Sets ---")
frozen = frozenset([1, 2, 3, 4])
print(f"Frozen Set: {frozen}")
# frozen.add(5)  # This WILL raise an AttributeError!
print("Frozen sets are immutable and can be used as dictionary keys or elements of other sets.")


# 6. Common Operations
print("\n--- Common Operations ---")
s = {10, 20, 30, 40, 50}
print(f"Length: {len(s)}")
print(f"Min: {min(s)}")
print(f"Max: {max(s)}")
print(f"Sum: {sum(s)}")
print(f"Membership (20 in s): {20 in s}")
