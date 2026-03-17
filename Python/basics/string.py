"""
Python Strings - Indexing, Slicing, Methods, and Formatting
"""

# 1. String Creation
print("--- Creating Strings ---")
single_quote_str = 'Hello'
double_quote_str = "World"
multiline_str = """This is a
string that spans
multiple lines!"""

print(f"{single_quote_str} {double_quote_str}")

# 2. String Concatenation and Repetition
print("\n--- Concatenation & Repetition ---")
greeting = "Hello" + " " + "Python" # Concatenation (adding strings)
print(greeting)

echo = "Echo! " * 3 # Repetition
print(echo)

# 3. Indexing
# Strings are ordered sequences of characters. You can access individual characters using [].
# Indexing starts at 0. Python also supports negative indexing (starts from the end).
print("\n--- String Indexing ---")
word = "PYTHON"
# P(0) Y(1) T(2) H(3) O(4) N(5)
# P(-6) Y(-5) T(-4) H(-3) O(-2) N(-1)

print(f"First character (0): {word[0]}")
print(f"Third character (2): {word[2]}")
print(f"Last character (-1): {word[-1]}")

# 4. Slicing
# Slicing allows you to grab a subsection of the string using the syntax [start:stop:step]
# - start is inclusive (default 0)
# - stop is EXCLUSIVE (up to, but not including) (default end of string)
# - step is the jump size (default 1)
print("\n--- String Slicing ---")
alphabet = "abcdefghijklmnopqrstuvwxyz"

print(f"Slice from index 2 to 5 [2:5]: {alphabet[2:5]}") # 'cde'
print(f"Slice from beginning up to index 5 [:5]: {alphabet[:5]}") # 'abcde'
print(f"Slice from index 5 to the end [5:]: {alphabet[5:]}") # 'fghi...'
print(f"Slice from index 2 to 10 by steps of 2 [2:10:2]: {alphabet[2:10:2]}") # 'cegi'
print(f"Reverse a string [::-1]: {alphabet[::-1]}") # Reverse the string

# 5. String Properties (Immutability)
print("\n--- String Immutability ---")
# Strings are immutable! Once created, you cannot change parts of them.
my_str = "Sam"
# my_str[0] = "P"  # THIS WILL THROW A TYPE ERROR!
# Instead, you must build a new string:
new_str = "P" + my_str[1:]
print(f"Changed string using slicing and concatenation: {new_str}")

# 6. String Methods
print("\n--- Common String Methods ---")
text = "hello world! learning Python is fun."

print(f"Uppercase: {text.upper()}")
print(f"Capitalize (first letter only): {text.capitalize()}")
print(f"Title Case: {text.title()}")
print(f"Split string into a list by spaces: {text.split()}")

csv_data = "apple,banana,cherry"
print(f"Split by comma: {csv_data.split(',')}")

# 7. Print Formatting
print("\n--- Print Formatting ---")
name = "Jose"
age = 29

# Oldest way: % Formatting (usually avoided now)
print("Hello, my name is %s and I am %s years old." % (name, age))

# Newer way: .format() method (very flexible)
print("Hello, my name is {} and I am {} years old.".format(name, age))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick")) # By keyword

# Float formatting with .format() -> {value:width.precision f}
result = 100 / 777
print("The result is {r:1.3f}".format(r=result))

# Newest way: f-Strings (Formatted String Literals - Python 3.6+)
# (Highly recommended for modern Python)
print(f"Hello, my name is {name} and I am {age} years old.")
# Float formatting with f-strings
print(f"The result is {result:1.3f}")
