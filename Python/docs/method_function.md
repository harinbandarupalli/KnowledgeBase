# Python Methods & Functions Guide

This document covers the two core building blocks for organizing and reusing code in Python: **Methods** and **Functions**.

---

## Methods vs Functions — What's the Difference?

| | Function | Method |
|---|---|---|
| **How to call** | Standalone: `len(my_list)` | Dot notation: `my_list.sort()` |
| **Belongs to** | No object | A specific object/type |
| **Examples** | `print()`, `len()`, `type()`, `range()` | `"hello".upper()`, `[1,2].append(3)` |

**Script:** [methods.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/methods.py)

### Topics Covered in `methods.py`:
- String methods: `.strip()`, `.lower()`, `.upper()`, `.replace()`, `.split()`, `.join()`, `.find()`, `.startswith()`, `.isdigit()`, `.center()`, `.zfill()`
- List methods: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`, `.count()`, `.index()`, `.copy()`, `.clear()`
- Dictionary methods: `.keys()`, `.values()`, `.items()`, `.get()`, `.pop()`, `.update()`, `.setdefault()`
- Set methods: `.add()`, `.discard()`, `.union()`, `.intersection()`
- **Discovering methods:** Using `dir()` and `help()` to explore any object

---

## Functions — Reusable Logic with `def`

**Script:** [functions.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/functions.py)

### 1. The `def` Keyword
Functions are defined with `def`, followed by the function name and parentheses:
```python
def greet():
    print("Hello!")
```

### 2. Parameters, Arguments, and Return Values
```python
def add(a, b):       # a, b are parameters
    return a + b

result = add(10, 20) # 10, 20 are arguments
```
- **Default parameters:** `def greet(name, greeting="Hello")`
- **Keyword arguments:** `greet(greeting="Hi", name="Alice")`

### 3. `*args` and `**kwargs`
- `*args` accepts any number of positional arguments as a **tuple**
- `**kwargs` accepts any number of keyword arguments as a **dictionary**
```python
def func(*args, **kwargs):
    print(args)    # (1, 2, 3)
    print(kwargs)  # {'x': 10, 'y': 20}

func(1, 2, 3, x=10, y=20)
```

### 4. Logic in Functions
- Using `if/elif/else` inside functions
- Early return pattern (exit as soon as you have the answer)
- Functions that return `True`/`False` (predicates like `is_even()`)

### 5. Tuple Unpacking with Functions
Functions can return multiple values as a tuple, which you can unpack:
```python
def get_stats(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

low, high, avg = get_stats([10, 20, 30])
```

### 6. Interactions Between Functions
- Passing functions as arguments to other functions
- Chaining/piping function calls
- Nested helper functions (inner functions)

### 7. Type Hints & Docstrings
Modern Python uses type hints and docstrings for clarity:
```python
def calculate_area(length: float, width: float) -> float:
    """Returns the area of a rectangle."""
    return length * width
```
