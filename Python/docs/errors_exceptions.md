# Errors, Exceptions & Testing in Python

This document covers Python's error handling system, code quality tools, and the built-in testing framework.

---

## Scripts

| # | Topic | File |
|---|-------|------|
| 1 | Errors & Exception Handling | [errors_exceptions.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/errors_exceptions.py) |
| 2 | Pylint / Ruff Overview | [pylint_overview.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/pylint_overview.py) |
| 3 | Unittest Testing | [unittest_testing.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/unittest_testing.py) |

---

## 1. Exception Handling

### The try/except Pattern
```python
try:
    result = 10 / 0             # Code that might fail
except ZeroDivisionError as e:
    print(f"Error: {e}")        # Handle the error
else:
    print(f"Success: {result}") # Only runs if NO exception
finally:
    print("Always runs")        # Cleanup (close files, etc.)
```

### Common Exception Types

| Exception | Cause |
|-----------|-------|
| `SyntaxError` | Invalid Python syntax |
| `NameError` | Undefined variable |
| `TypeError` | Wrong type for operation |
| `ValueError` | Right type, wrong value |
| `IndexError` | List index out of range |
| `KeyError` | Dict key not found |
| `FileNotFoundError` | File doesn't exist |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Object has no such method |

### Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age
```

### Custom Exceptions
```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw ${amount}. Balance: ${balance}")
```

### Best Practices
1. Catch **specific** exceptions, never bare `except:`
2. Use `else` for success-only code
3. Use `finally` for cleanup (files, connections)
4. Keep `try` blocks as small as possible
5. Create custom exceptions for domain errors
6. Chain exceptions with `raise ... from ...`

---

## 2. Pylint & Ruff (Code Quality)

### Pylint Message Categories

| Code | Category | Meaning |
|------|----------|---------|
| **C** | Convention | PEP 8 style violations |
| **R** | Refactor | Code simplification suggestions |
| **W** | Warning | Unused imports/variables, potential issues |
| **E** | Error | Probable bugs |
| **F** | Fatal | Cannot analyze the file |

### Running Linters
```bash
# Pylint
pip install pylint
pylint my_script.py

# Ruff (modern, 10-100x faster)
pip install ruff
ruff check .            # Check for issues
ruff check --fix .      # Auto-fix issues
ruff format .           # Format code
```

### Disabling Warnings
```python
x = 5  # pylint: disable=invalid-name     # Inline
```
```toml
# pyproject.toml
[tool.ruff.lint]
select = ["E", "F", "W", "I", "N", "UP"]
```

---

## 3. Unittest — Built-in Testing

### Basic Test Structure
```python
import unittest

class TestMyFunction(unittest.TestCase):
    def setUp(self):
        """Runs before EACH test method."""
        self.data = [1, 2, 3]

    def test_sum(self):
        self.assertEqual(sum(self.data), 6)

    def test_length(self):
        self.assertEqual(len(self.data), 3)

    def tearDown(self):
        """Runs after EACH test method."""
        pass

if __name__ == "__main__":
    unittest.main()
```

### Assert Method Reference

| Method | Checks |
|--------|--------|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIs(a, b)` | `a is b` |
| `assertIsNone(x)` | `x is None` |
| `assertIn(a, b)` | `a in b` |
| `assertIsInstance(a, b)` | `isinstance(a, b)` |
| `assertAlmostEqual(a, b)` | `round(a-b, 7) == 0` |
| `assertRaises(exc)` | Function raises `exc` |
| `assertGreater(a, b)` | `a > b` |

### Running Tests
```bash
python -m unittest test_file.py              # Run file
python -m unittest test_file.TestClass       # Run class
python -m unittest discover                  # Auto-discover
python -m unittest -v test_file.py           # Verbose
```

> **Note:** For larger projects, consider **pytest** — it's simpler, more powerful, and the industry standard. Install with `pip install pytest` and run with `pytest`.
