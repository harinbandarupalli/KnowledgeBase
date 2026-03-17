"""
Python Methods - Built-in Methods and Using Python Documentation
"""

# 1. What is a Method?
# A method is a function that belongs to an object. You call it with dot notation: object.method()
# A function is standalone (e.g., len(), print()). A method is attached to a type.
print("--- Methods vs Functions ---")
my_list = [3, 1, 2]

# len() is a FUNCTION — called on its own
print(f"len(my_list) = {len(my_list)}")

# .sort() is a METHOD — called ON the list object
my_list.sort()
print(f"my_list.sort() -> {my_list}")


# 2. String Methods
print("\n--- String Methods ---")
text = "  Hello, World!  "

print(f"Original:        '{text}'")
print(f".strip():        '{text.strip()}'")       # Remove leading/trailing whitespace
print(f".lstrip():       '{text.lstrip()}'")       # Remove leading whitespace
print(f".rstrip():       '{text.rstrip()}'")       # Remove trailing whitespace
print(f".lower():        '{text.strip().lower()}'")
print(f".upper():        '{text.strip().upper()}'")
print(f".title():        '{text.strip().title()}'")
print(f".replace('World', 'Python'): '{text.strip().replace('World', 'Python')}'")
print(f".startswith('  He'): {text.startswith('  He')}")
print(f".endswith('!  '): {text.endswith('!  ')}")
print(f".find('World'): {text.find('World')}")     # Returns index or -1
print(f".count('l'): {text.count('l')}")
print(f".isdigit(): {'123'.isdigit()}")
print(f".isalpha(): {'abc'.isalpha()}")
print(f".split(','): {text.strip().split(',')}")
print(f"', '.join(['a','b','c']): {', '.join(['a', 'b', 'c'])}")
print(f".center(30, '-'): '{text.strip().center(30, '-')}'")
print(f".zfill(20): '{'42'.zfill(20)}'")


# 3. List Methods
print("\n--- List Methods ---")
nums = [5, 2, 8, 1, 9]
print(f"Original: {nums}")

nums.append(10)
print(f".append(10):  {nums}")

nums.insert(0, 99)
print(f".insert(0,99): {nums}")

nums.remove(99)
print(f".remove(99):  {nums}")

popped = nums.pop()
print(f".pop():       {nums}, returned {popped}")

nums.sort()
print(f".sort():      {nums}")

nums.reverse()
print(f".reverse():   {nums}")

print(f".count(5):    {nums.count(5)}")
print(f".index(8):    {nums.index(8)}")

nums2 = nums.copy()
print(f".copy():      {nums2}")

nums.clear()
print(f".clear():     {nums}")


# 4. Dictionary Methods
print("\n--- Dictionary Methods ---")
d = {"name": "Alice", "age": 30, "city": "NYC"}

print(f".keys():   {list(d.keys())}")
print(f".values(): {list(d.values())}")
print(f".items():  {list(d.items())}")
print(f".get('name'):      {d.get('name')}")
print(f".get('phone','N/A'): {d.get('phone', 'N/A')}")
print(f".pop('city'):      {d.pop('city')}")
print(f"After pop: {d}")

d.update({"email": "alice@example.com", "age": 31})
print(f".update(): {d}")

d.setdefault("country", "USA")
print(f".setdefault('country','USA'): {d}")


# 5. Set Methods
print("\n--- Set Methods ---")
s = {1, 2, 3}
print(f".add(4): ", end=""); s.add(4); print(s)
print(f".discard(2): ", end=""); s.discard(2); print(s)
print(f".union({{5,6}}): {s.union({5, 6})}")
print(f".intersection({{1,3,5}}): {s.intersection({1, 3, 5})}")


# 6. How to Discover Methods
print("\n--- Discovering Methods ---")
print("Use dir() to list all methods of an object:")
print(f"  dir('hello')[:10] = {dir('hello')[:10]}...")
print()
print("Use help() for documentation on a specific method:")
print("  help(str.upper)  # Run this in a Python REPL for full docs")
print()
print("Tip: In an IDE or Jupyter, type 'object.' then press Tab for autocomplete.")
print("Tip: Use Shift+Tab in Jupyter for inline docstrings.")
