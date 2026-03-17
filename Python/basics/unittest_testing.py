"""
Running Tests with the Unittest Library
"""
import unittest


# ============================================================
# 1. What is Unittest?
# ============================================================
# unittest is Python's built-in testing framework.
# Tests verify that your code works as expected.
# Run tests with: python -m unittest test_file.py
#            or:  python -m unittest discover


# ============================================================
# 2. Code to Test
# ============================================================
def add(a, b):
    """Add two numbers."""
    return a + b

def divide(a, b):
    """Divide a by b. Raises ValueError for division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_palindrome(text):
    """Check if a string is a palindrome (case-insensitive)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def capitalize_name(name):
    """Capitalize first and last name."""
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    return name.strip().title()


# ============================================================
# 3. Basic Test Class
# ============================================================
class TestAdd(unittest.TestCase):
    """Tests for the add function."""

    def test_add_positive(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        """Test adding negative numbers."""
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        """Test adding zero."""
        self.assertEqual(add(5, 0), 5)

    def test_add_floats(self):
        """Test adding floats."""
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)


# ============================================================
# 4. Testing Exceptions
# ============================================================
class TestDivide(unittest.TestCase):
    """Tests for the divide function."""

    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_float_result(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333, places=3)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_by_zero_message(self):
        """Test the exception message."""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")


# ============================================================
# 5. Common Assert Methods
# ============================================================
class TestPalindrome(unittest.TestCase):
    """Tests demonstrating various assert methods."""

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_case_insensitive(self):
        self.assertTrue(is_palindrome("Racecar"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("nurses run"))


class TestCapitalize(unittest.TestCase):

    def test_capitalize(self):
        self.assertEqual(capitalize_name("john doe"), "John Doe")

    def test_capitalize_strips_whitespace(self):
        self.assertEqual(capitalize_name("  alice smith  "), "Alice Smith")

    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            capitalize_name("")

    def test_result_is_string(self):
        self.assertIsInstance(capitalize_name("test"), str)

    def test_none_raises(self):
        with self.assertRaises((ValueError, AttributeError)):
            capitalize_name(None)


# ============================================================
# 6. setUp and tearDown
# ============================================================
class TestWithSetup(unittest.TestCase):
    """setUp runs BEFORE each test, tearDown runs AFTER each test."""

    def setUp(self):
        """Create test data before each test."""
        self.numbers = [1, 2, 3, 4, 5]
        self.empty_list = []

    def tearDown(self):
        """Clean up after each test (close files, connections, etc.)."""
        pass  # Nothing to clean up in this example

    def test_sum(self):
        self.assertEqual(sum(self.numbers), 15)

    def test_length(self):
        self.assertEqual(len(self.numbers), 5)

    def test_empty(self):
        self.assertEqual(len(self.empty_list), 0)


# ============================================================
# 7. Assert Method Reference
# ============================================================
# assertEqual(a, b)          a == b
# assertNotEqual(a, b)       a != b
# assertTrue(x)              bool(x) is True
# assertFalse(x)             bool(x) is False
# assertIs(a, b)             a is b
# assertIsNot(a, b)          a is not b
# assertIsNone(x)            x is None
# assertIsNotNone(x)         x is not None
# assertIn(a, b)             a in b
# assertNotIn(a, b)          a not in b
# assertIsInstance(a, b)     isinstance(a, b)
# assertAlmostEqual(a, b)    round(a-b, 7) == 0
# assertRaises(exc)          Function raises exc
# assertGreater(a, b)        a > b
# assertLess(a, b)           a < b


# ============================================================
# 8. Running Tests
# ============================================================
# Command line:
#   python -m unittest test_file.py           # Run specific file
#   python -m unittest test_file.TestClass    # Run specific class
#   python -m unittest discover               # Auto-discover all tests
#   python -m unittest -v test_file.py        # Verbose output
#
# In this file:
if __name__ == "__main__":
    unittest.main(verbosity=2)
