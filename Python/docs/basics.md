# Python Basics Tutorial

Welcome to the Python basics learning module! This folder contains a set of scripts designed to walk you through the fundamental building blocks of the Python programming language.

Below is a breakdown of the core topics covered, along with direct links to the executable Python scripts. You can run these scripts in your terminal to see the outputs in action.

---

## 🔢 1. Python Numbers
**File:** [`numbers.py`](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/numbers.py)

This script covers the two primary numerical data types in Python: **Integers** (whole numbers) and **Floating Point Numbers** (decimals). 

**Key Concepts Covered:**
- Basic Arithmetic Operations (`+`, `-`, `*`, `/`)
- Floor Division (`//`), which truncates decimals to integers
- Modulo (`%`), which returns the remainder of a division (useful for checking even/odd numbers)
- Exponentiation (`**`)
- Understanding the Order of Operations (PEMDAS)
- Useful built-in number functions like `abs()` and `round()`

---

## 📝 2. Variable Assignments
**File:** [`variable.py`](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/variable.py)

Variables allow us to store data in our computer's memory under a familiar name. 

**Key Concepts Covered:**
- Variable assignment using the `=` operator
- **Dynamic Typing:** Understanding how Python can easily change course and reassign a variable from one data type (like an Integer) to another (like a String) dynamically.
- Best practices and strict rules for naming variables.
- Performing math dynamically using variable expressions.
- Multiple assignment syntax.

---

## 🧵 3. Introduction to Strings
**File:** [`string.py`](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/string.py)

Strings are ordered sequences of characters used to represent text. Because they are a sequence, Python offers powerful tools to inspect and modify text data.

**Key Concepts Covered:**
- **String Creation:** Differences between single, double, and multiline string quotes.
- **Indexing:** Accessing individual characters in a string using positive (e.g., `[0]`) and negative (e.g., `[-1]`) index numbers.
- **Slicing:** Using the syntax `[start:stop:step]` to extract a subset of characters from a string. Includes reversing elements (`[::-1]`).
- **Immutability:** Discovering why you can't re-assign elements directly within a string.
- **Concatenation and Repetition:** Expanding strings via concatenation (`+`) and repeating via multiplication (`*`).
- **String Methods:** Leveraging built-in functions like `.upper()`, `.lower()`, and `.split()`.
- **Print Formatting:** Formatting strings for output, covering `.format()` and the newer, highly-recommended **f-strings**.

---

## 📋 4. Lists
**File:** [lists.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/lists.py)

Lists are ordered, mutable sequences — the most versatile data structure in Python.

**Key Concepts Covered:**
- Creating lists (simple, mixed-type, and nested)
- Indexing and Slicing (same syntax as strings)
- **Mutability:** Unlike strings, list elements can be reassigned directly.
- List Methods: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`, `.extend()`, `.count()`, `.index()`
- **List Comprehensions:** Writing concise one-liner expressions to generate lists.
- Common operations: `len()`, `min()`, `max()`, `sum()`, `in`, concatenation (`+`), and repetition (`*`)

---

## 📖 5. Dictionaries
**File:** [dictionaries.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/dictionaries.py)

Dictionaries are unordered mappings that store data as **key-value pairs**, optimized for fast lookups.

**Key Concepts Covered:**
- Creating dictionaries with `{key: value}` syntax
- Accessing values with `[]` and the safer `.get()` method
- Adding, updating, and deleting key-value pairs (`del`, `.pop()`)
- Dictionary Methods: `.keys()`, `.values()`, `.items()`
- Iterating through dictionaries
- **Nested Dictionaries:** Dictionaries within dictionaries
- **Dictionary Comprehensions**
- Merging dictionaries with the `|` operator (Python 3.9+)

---

## 📦 6. Tuples
**File:** [tuples.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/tuples.py)

Tuples are ordered, **immutable** sequences — like lists that cannot be changed after creation.

**Key Concepts Covered:**
- Creating tuples (including the single-element tuple gotcha with the trailing comma)
- Indexing and Slicing
- **Immutability:** Why tuples cannot be modified and when that's useful.
- Tuple Methods: `.count()` and `.index()`
- **Tuple Unpacking:** Assigning elements to multiple variables in one line, including the `*` star expression.
- **Tuples vs Lists:** When to use which type.
- Converting between lists and tuples

---

## 🔗 7. Sets
**File:** [sets.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/sets.py)

Sets are unordered collections of **unique elements** — perfect for removing duplicates and performing mathematical set operations.

**Key Concepts Covered:**
- Creating sets and automatic duplicate removal
- Creating a set from a list to find unique items
- Adding (`.add()`) and removing (`.discard()`, `.remove()`) elements
- **Set Operations:** Union (`|`), Intersection (`&`), Difference (`-`), Symmetric Difference (`^`)
- **Subset and Superset checks:** `.issubset()`, `.issuperset()`, `.isdisjoint()`
- **Frozen Sets:** Immutable sets that can be used as dictionary keys

---

## ✅ 8. Booleans
**File:** [booleans.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/booleans.py)

Booleans (`True`/`False`) are the foundation of all conditional logic in Python.

**Key Concepts Covered:**
- Boolean basics and their relationship to integers (`True=1`, `False=0`)
- **Comparison Operators:** `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators:** `and`, `or`, `not`
- **Truthiness and Falsiness:** Which values Python considers `True` or `False` (e.g., empty lists are falsy)
- **Identity Operators:** `is` vs `==` (object identity vs value equality)
- **Membership Operators:** `in`, `not in`

---

## 📁 9. File I/O
**File:** [file_io.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/file_io.py)

Reading and writing files is essential for any real-world Python application.

**Key Concepts Covered:**
- **Writing:** Creating and writing to files with `open(path, 'w')`
- **Reading:** Reading entire files (`.read()`), line by line, and into a list (`.readlines()`)
- **Appending:** Adding data to the end of existing files with `'a'` mode
- **The `with` statement:** Using context managers to safely auto-close files
- **File Modes Summary:** `'r'`, `'w'`, `'a'`, `'r+'`, `'rb'`, `'wb'`
- **File Path Operations:** Using `os.path` to check existence, get directory/file names, and extensions

---

## 🔀 11. If, Elif, and Else Statements
**File:** [if_elif_else.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/if_elif_else.py)

Control flow allows your programs to make decisions based on conditions.

**Key Concepts Covered:**
- Basic `if`, `if/else`, and `if/elif/else` chains
- Nested if statements
- Combining conditions with `and`, `or`, `not`
- **Ternary Operator:** One-line `if/else` expressions
- Truthiness in conditions (empty lists, `None`, etc.)
- **Match Statement** (Python 3.10+): Structural pattern matching (like switch/case)

---

## 🔄 12. For Loops
**File:** [for_loops.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/for_loops.py)

For loops iterate over sequences (lists, strings, ranges, dictionaries).

**Key Concepts Covered:**
- Looping through lists and strings
- `range()` with start, stop, and step arguments
- `enumerate()` for getting index and value simultaneously
- `zip()` for looping over multiple lists in parallel
- Nested for loops
- `break` and `continue` statements
- `for...else` pattern (runs when loop completes without `break`)
- Iterating through dictionary keys, values, and items
- Tuple unpacking inside loops

---

## 🔁 13. While Loops
**File:** [while_loops.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/while_loops.py)

While loops repeat as long as a condition remains True — useful when you don't know how many iterations you need.

**Key Concepts Covered:**
- Basic while loop with counter
- `while...else` pattern
- `break` and `continue` in while loops
- Sentinel value pattern
- Input validation pattern
- Avoiding infinite loops (safety patterns with max iterations)
- **While vs For:** When to choose which loop type

---

## 🧰 14. Useful Operators
**File:** [operators.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/operators.py)

Python provides many powerful built-in operators and functions that make code more concise and expressive.

**Key Concepts Covered:**
- `range()`, `enumerate()`, `zip()`
- `in` operator for membership testing
- `min()`, `max()`, `sum()`, `abs()`, `round()` with custom `key` functions
- `sorted()` and `reversed()`
- **lambda functions:** Anonymous one-line functions
- `map()` and `filter()` for functional-style programming
- `any()` and `all()` for boolean aggregation
- **Walrus Operator** `:=` (Python 3.8+)
- Unpacking operators `*` and `**`

---

## 🧩 15. List Comprehensions
**File:** [list_comprehensions.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/list_comprehensions.py)

Comprehensions are a concise, Pythonic way to create and transform collections in a single line.

**Key Concepts Covered:**
- Basic list comprehensions (`[expr for item in iterable]`)
- Comprehensions with filtering (`if` condition)
- Comprehensions with `if/else` transforms
- Nested comprehensions (flattening matrices)
- String operations with comprehensions
- **Dictionary Comprehensions** (`{key: val for ...}`)
- **Set Comprehensions** (`{expr for ...}`)
- **Generator Expressions** (`(expr for ...)`) for memory-efficient processing
- When NOT to use comprehensions (readability guidelines)

---

## 🔧 16. Methods and Python Documentation
**File:** [methods.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/methods.py)
**Full Guide:** [method_function.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/method_function.md)

Methods are functions that belong to an object, called with dot notation (`object.method()`).

**Key Concepts Covered:**
- Methods vs functions — what's the difference
- All common **string methods** (`.strip()`, `.replace()`, `.split()`, `.join()`, `.find()`, `.isdigit()`, etc.)
- All common **list methods** (`.append()`, `.insert()`, `.pop()`, `.sort()`, `.reverse()`, `.copy()`, `.clear()`)
- **Dictionary methods** (`.keys()`, `.values()`, `.items()`, `.get()`, `.update()`, `.setdefault()`)
- **Set methods** (`.add()`, `.discard()`, `.union()`, `.intersection()`)
- **Discovering methods:** Using `dir()` and `help()` to explore any object

---

## ⚙️ 17. Functions
**File:** [functions.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/functions.py)
**Full Guide:** [method_function.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/method_function.md)

Functions are reusable blocks of code defined with the `def` keyword.

**Key Concepts Covered:**
- The `def` keyword and calling functions
- Parameters, arguments, default values, and keyword arguments
- `return` statements
- `*args` (variable positional arguments) and `**kwargs` (variable keyword arguments)
- Logic inside functions (conditionals, early return pattern)
- **Tuple unpacking** with function return values
- **Function interactions:** Passing functions as arguments, chaining calls, nested helper functions
- **Type hints** and **docstrings** for modern, well-documented code

---

## 🏗️ 18. OOP — Classes, Attributes & Methods
**File:** [oop_classes_attributes.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/oop_classes_attributes.py)
**Full Guide:** [OOPS.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/OOPS.md)

Object Oriented Programming lets you create custom types that bundle data and behavior together.

**Key Concepts Covered:**
- The `class` keyword and creating instances
- `__init__` constructor and the `self` parameter
- **Class attributes** (shared by all instances) vs **instance attributes** (unique per object)
- Instance methods — functions that operate on an object's data
- Modifying attributes through methods (e.g., `BankAccount.deposit()`)

---

## 🧬 19. OOP — Inheritance & Polymorphism
**File:** [oop_inheritance_polymorphism.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/oop_inheritance_polymorphism.py)
**Full Guide:** [OOPS.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/OOPS.md)

Inheritance lets a child class reuse and extend a parent class. Polymorphism enables the same interface to work with different types.

**Key Concepts Covered:**
- Basic inheritance with `super().__init__()`
- Method overriding — child redefines a parent method
- Polymorphism — same method name, different behavior per class
- `isinstance()` and `issubclass()` checks
- Multiple inheritance and Method Resolution Order (MRO)

---

## ✨ 20. OOP — Special (Magic/Dunder) Methods
**File:** [oop_dunder_methods.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/oop_dunder_methods.py)
**Full Guide:** [OOPS.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/OOPS.md)

Dunder methods let you hook your custom classes into Python's built-in operators and functions.

**Key Concepts Covered:**
- `__str__` and `__repr__` for printing objects
- `__len__` for `len()` support
- `__getitem__` for indexing (`obj[i]`)
- `__eq__`, `__lt__`, `__gt__` for comparisons and sorting
- `__add__`, `__sub__`, `__mul__` for arithmetic operators
- `__contains__` for `in` keyword support
- `__bool__` for truthiness control

---

## 📦 22. Collections Module
**File:** [collections_module.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/collections_module.py)
**Full Guide:** [advanced_modules.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/advanced_modules.md)

Specialized container data types beyond the built-in list, dict, and set.

**Key Concepts Covered:**
- `Counter` — count occurrences of elements
- `defaultdict` — dictionary with default values (no more `KeyError`)
- `OrderedDict` — dict with `move_to_end()` and order-aware equality
- `namedtuple` — lightweight, immutable objects with named fields
- `deque` — double-ended queue with fast appends/pops from both sides

---

## 📂 23. OS Module — Files & Folders
**File:** [os_module.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/os_module.py)
**Full Guide:** [advanced_modules.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/advanced_modules.md)

Navigate, create, modify, and inspect files and directories programmatically.

**Key Concepts Covered:**
- `os.getcwd()`, `os.listdir()`, `os.path.join()`
- `os.path.exists()`, `isfile()`, `isdir()`
- `os.walk()` for recursive directory traversal
- Creating (`makedirs`) and removing (`rmtree`) directories
- File operations: rename, copy, move, delete
- Environment variables with `os.environ`

---

## 📅 24. Datetime Module
**File:** [datetime_module.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/datetime_module.py)
**Full Guide:** [advanced_modules.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/advanced_modules.md)

Create, format, parse, and do arithmetic with dates and times.

**Key Concepts Covered:**
- `datetime.now()`, `date.today()`, accessing year/month/day/hour
- **strftime** (date → string) and **strptime** (string → date)
- `timedelta` for date arithmetic (add/subtract days, weeks, hours)
- Comparing dates and calculating differences
- `calendar` module (leap years, month ranges)

---

## 🔢 25. Math & Random Modules
**File:** [math_random_module.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/math_random_module.py)
**Full Guide:** [advanced_modules.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/advanced_modules.md)

Mathematical operations and random number generation.

**Key Concepts Covered:**
- **Math:** constants (`pi`, `e`), `floor`/`ceil`, `sqrt`, `log`, `factorial`, `gcd`, `comb`/`perm`, trig functions
- **Random:** `random()`, `randint()`, `uniform()`, `choice()`, `choices(weights=...)`, `sample()`, `shuffle()`
- Gaussian distribution, seeding for reproducibility

---

## 🐛 26. Python Debugger (pdb)
**File:** [debugger_pdb.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/debugger_pdb.py)
**Full Guide:** [advanced_modules.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/advanced_modules.md)

Interactive debugging to pause execution, inspect variables, and step through code.

**Key Concepts Covered:**
- `breakpoint()` (Python 3.7+) and `pdb.set_trace()`
- Essential commands: `n` (next), `s` (step), `c` (continue), `p` (print), `b` (breakpoint)
- Conditional breakpoints
- Post-mortem debugging after exceptions
- IDE debuggers (VS Code, PyCharm)

---

## 🔍 27. Regular Expressions (re)
**File:** [regex_module.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/regex_module.py)
**Full Guide:** [advanced_modules.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/advanced_modules.md)

Pattern matching for searching, extracting, and replacing text.

**Key Concepts Covered:**
- `re.search()`, `re.match()`, `re.findall()`, `re.finditer()`
- Patterns: `\d`, `\w`, `\s`, quantifiers `+`, `*`, `?`, `{n}`
- Greedy vs non-greedy matching
- Groups and named groups for extracting parts
- `re.sub()` for find-and-replace, `re.split()` for splitting
- `re.compile()` for reusable patterns
- Real-world patterns (email, phone, URL, IP)

---

## ⏱️ 28. Timing Your Python Code
**File:** [timing_code.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/timing_code.py)
**Full Guide:** [advanced_modules.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/advanced_modules.md)

Measure and compare the performance of your code.

**Key Concepts Covered:**
- `time.perf_counter()` for simple timing
- `timeit.timeit()` for reliable benchmarks (averages over many runs)
- Comparing approaches: for-loop vs comprehension vs `map()`
- String concatenation performance (`+=` vs `join`)
- Creating a `@timer` decorator for automatic function timing

---

## 🗜️ 29. Zipping & Unzipping Files
**File:** [zip_unzip.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/zip_unzip.py)
**Full Guide:** [advanced_modules.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/advanced_modules.md)

Create, read, and extract compressed zip archives programmatically.

**Key Concepts Covered:**
- Creating zip files with `zipfile.ZipFile("w")`
- Listing and inspecting archive contents
- Extracting all files or a single file
- Reading files directly from a zip (without extracting)
- Appending to existing archives
- `shutil.make_archive()` for quick one-line archiving

---

## 🚨 31. Errors & Exception Handling
**File:** [errors_exceptions.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/errors_exceptions.py)
**Full Guide:** [errors_exceptions.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/errors_exceptions.md)

Gracefully handle errors so your programs don't crash unexpectedly.

**Key Concepts Covered:**
- Common exception types (`ValueError`, `TypeError`, `KeyError`, `IndexError`, etc.)
- `try` / `except` / `else` / `finally` pattern
- Catching multiple and all exceptions
- **Raising exceptions** with `raise`
- **Custom exceptions** (creating your own error classes)
- Exception chaining with `raise ... from ...`
- Best practices for error handling

---

## 🔎 32. Pylint & Code Quality
**File:** [pylint_overview.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/pylint_overview.py)
**Full Guide:** [errors_exceptions.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/errors_exceptions.md)

Static analysis tools that check your code for bugs and style issues without running it.

**Key Concepts Covered:**
- Pylint message categories: Convention, Refactor, Warning, Error, Fatal
- Common pylint messages and what they mean
- Disabling specific warnings (inline and in config)
- **Ruff** — the modern, faster alternative (10-100x faster than pylint)

---

## 🧪 33. Unittest — Testing Your Code
**File:** [unittest_testing.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/unittest_testing.py)
**Full Guide:** [errors_exceptions.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/errors_exceptions.md)

Python's built-in testing framework for verifying your code works correctly.

**Key Concepts Covered:**
- Creating test classes with `unittest.TestCase`
- Assert methods: `assertEqual`, `assertTrue`, `assertRaises`, `assertAlmostEqual`, etc.
- `setUp()` and `tearDown()` for test setup/cleanup
- Testing exceptions with `assertRaises`
- Running tests from the command line
- Note on **pytest** as the industry-standard alternative

---

## ⚡ 34. Big O Notation & Data Structure Performance
**File:** [BigO.md](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/docs/BigO.md)

Understanding time complexity is critical for writing efficient code. The Big O reference document contains detailed tables showing the **average and worst-case performance** of every common operation for Lists, Dictionaries, Tuples, and Sets.

**External References:**
- [Python Wiki: Time Complexity](https://wiki.python.org/moin/TimeComplexity) — Official CPython complexity guarantees
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/) — Visual reference for all data structures and algorithms
