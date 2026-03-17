"""
Pylint Overview - Code Quality and Linting
"""

# ============================================================
# 1. What is Pylint?
# ============================================================
# Pylint is a static code analysis tool that checks your Python code for:
# - Errors (bugs that would crash at runtime)
# - Style violations (PEP 8 conventions)
# - Code smells (bad patterns, unused variables, etc.)
# - Refactoring suggestions

print("--- What is Pylint? ---")
print("  Pylint checks your code WITHOUT running it.")
print("  It catches bugs, style issues, and suggests improvements.")
print()

# ============================================================
# 2. Installing and Running Pylint
# ============================================================
print("--- Installation & Usage ---")
print("  Install:  pip install pylint")
print("  Run:      pylint my_script.py")
print("  Rate:     pylint gives a score out of 10.0")
print()

# ============================================================
# 3. Understanding Pylint Messages
# ============================================================
print("--- Message Categories ---")
categories = {
    "C (Convention)":   "Code style violations (PEP 8)",
    "R (Refactor)":     "Refactoring suggestions (simplify code)",
    "W (Warning)":      "Potential issues (unused imports, variables)",
    "E (Error)":        "Probable bugs (undefined variables, bad syntax)",
    "F (Fatal)":        "Errors preventing analysis (bad file, syntax errors)",
}
for cat, desc in categories.items():
    print(f"  {cat:22} -> {desc}")

print("\n--- Common Messages ---")
messages = {
    "C0114": "missing-module-docstring — Module has no docstring",
    "C0116": "missing-function-docstring — Function has no docstring",
    "C0103": "invalid-name — Variable name too short or doesn't match convention",
    "W0611": "unused-import — Imported module not used",
    "W0612": "unused-variable — Variable assigned but never used",
    "W0613": "unused-argument — Function argument never used",
    "E1101": "no-member — Object has no such attribute",
    "R0903": "too-few-public-methods — Class could be a dataclass/namedtuple",
    "R1705": "no-else-return — Unnecessary else after return",
}
for code, desc in messages.items():
    print(f"  {code}: {desc}")


# ============================================================
# 4. Disabling Specific Warnings
# ============================================================
print("\n--- Disabling Warnings ---")
print("  Inline (single line):")
print('    x = 5  # pylint: disable=invalid-name')
print()
print("  Inline (block):")
print('    # pylint: disable=missing-docstring')
print('    def my_func():')
print('        pass')
print('    # pylint: enable=missing-docstring')
print()
print("  In .pylintrc or pyproject.toml:")
print('    [tool.pylint.messages_control]')
print('    disable = ["C0114", "C0116", "R0903"]')


# ============================================================
# 5. Modern Alternative: Ruff
# ============================================================
print("\n--- Modern Alternative: Ruff ---")
print("  Ruff is a MUCH faster linter (10-100x) written in Rust.")
print("  It replaces: pylint, flake8, isort, pyflakes, and more.")
print()
print("  Install:  pip install ruff")
print("  Check:    ruff check .")
print("  Fix:      ruff check --fix .")
print("  Format:   ruff format .")
print()
print("  Configure in pyproject.toml:")
print('    [tool.ruff.lint]')
print('    select = ["E", "F", "W", "I", "N", "UP"]')


# ============================================================
# 6. Example Code for Linting Practice
# ============================================================
print("\n--- Example: Code with Issues ---")

# This code has intentional style issues for practice:
example = '''
import os         # W0611: unused import
import sys

def add(a,b):     # C0116: missing docstring, C0326: spacing
    x = 10        # W0612: unused variable
    return a+b

class foo:        # C0103: class name should be CamelCase
    pass
'''
print(example)
print("  Try running: pylint <filename>  or  ruff check <filename>")
print("  to see what issues are caught!")
