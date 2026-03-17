"""
Python Debugger (pdb) - Interactive Debugging
"""

# ============================================================
# 1. What is pdb?
# ============================================================
# pdb is Python's built-in interactive debugger.
# It lets you pause execution, inspect variables, step through code line by line.

# HOW TO USE:
# Option 1: Add a breakpoint in your code
#   import pdb; pdb.set_trace()       # Python 3.6 and earlier
#   breakpoint()                       # Python 3.7+ (preferred)
#
# Option 2: Run a script with the debugger
#   python -m pdb my_script.py
#
# Option 3: Post-mortem debugging (after an error)
#   python -m pdb -c continue my_script.py

print("--- Python Debugger (pdb) Commands ---")

# ============================================================
# 2. Essential pdb Commands
# ============================================================
commands = {
    "h (help)":       "Show help. 'h <command>' for specific help",
    "n (next)":       "Execute next line (step OVER function calls)",
    "s (step)":       "Step INTO a function call",
    "c (continue)":   "Continue execution until next breakpoint",
    "q (quit)":       "Quit the debugger",
    "p <expr>":       "Print the value of an expression",
    "pp <expr>":      "Pretty-print the value of an expression",
    "l (list)":       "Show source code around current line",
    "ll (longlist)":  "Show full source of current function",
    "w (where)":      "Show the call stack (traceback)",
    "u (up)":         "Move up one frame in the call stack",
    "d (down)":       "Move down one frame in the call stack",
    "b <line>":       "Set a breakpoint at a line number",
    "b <func>":       "Set a breakpoint at a function",
    "cl (clear)":     "Clear breakpoints",
    "r (return)":     "Continue until current function returns",
    "a (args)":       "Print the arguments of the current function",
    "!<statement>":   "Execute a Python statement (e.g., !x = 5)",
}

for cmd, desc in commands.items():
    print(f"  {cmd:20} -> {desc}")


# ============================================================
# 3. Example: Using breakpoint()
# ============================================================
print("\n--- Example Code (uncomment breakpoint() to try) ---")

def calculate_average(numbers):
    """Calculate average with a potential bug to debug."""
    total = 0
    for i, num in enumerate(numbers):
        total += num
        # Uncomment the next line to pause here during execution:
        # breakpoint()
    average = total / len(numbers)
    return average

data = [10, 20, 30, 40, 50]
result = calculate_average(data)
print(f"  Average of {data} = {result}")


# ============================================================
# 4. Conditional Breakpoints
# ============================================================
print("\n--- Conditional Breakpoints ---")
print("  In pdb, set conditional breakpoints like this:")
print("    b 25, x > 100     # Break at line 25 only when x > 100")
print()
print("  Or in code:")
print("    if x > 100:")
print("        breakpoint()  # Only pause when condition is met")


# ============================================================
# 5. Post-Mortem Debugging
# ============================================================
print("\n--- Post-Mortem Debugging ---")
print("  When an exception occurs, you can debug the crash:")
print("  $ python -m pdb -c continue my_script.py")
print("  This runs normally until an unhandled exception, then drops into pdb.")
print()
print("  In code:")
print("    import pdb")
print("    try:")
print("        risky_function()")
print("    except Exception:")
print("        pdb.post_mortem()  # Debug at the point of failure")


# ============================================================
# 6. IDE Debuggers
# ============================================================
print("\n--- IDE Debuggers (Recommended) ---")
print("  Modern IDEs provide visual debuggers that are easier to use:")
print("  • VS Code:    Click left of line number to set breakpoint, press F5")
print("  • PyCharm:    Click left of line number, Shift+F9 to debug")
print("  • Jupyter:    Use %debug magic command after an error")
print()
print("  IDE debuggers offer: variable inspection, watch expressions,")
print("  call stack visualization, and conditional breakpoints — all with a GUI.")
