"""
Python While Loops - Condition-Based Iteration
"""

# 1. Basic While Loop
# Keeps executing the block as long as the condition is True.
print("--- Basic While Loop ---")
count = 0
while count < 5:
    print(f"  Count: {count}")
    count += 1  # CRITICAL: Without this, the loop runs forever!

print(f"  Loop ended. Final count: {count}")


# 2. While with else
# The else block runs when the condition becomes False (NOT when you break).
print("\n--- While...Else ---")
x = 0
while x < 3:
    print(f"  x = {x}")
    x += 1
else:
    print(f"  While condition is now False. x = {x}")


# 3. break in While Loops
print("\n--- break ---")
while True:  # Infinite loop
    user_input = "quit"  # Simulated input
    if user_input == "quit":
        print("  User typed 'quit'. Breaking out of loop.")
        break
    # In real code, you'd process user_input here


# 4. continue in While Loops
print("\n--- continue ---")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  Odd number: {i}")


# 5. Sentinel Value Pattern
# Loop until a special "sentinel" value is encountered.
print("\n--- Sentinel Value Pattern ---")
data = [10, 20, 30, -1, 40, 50]  # -1 is the sentinel
index = 0
total = 0

while data[index] != -1:
    total += data[index]
    index += 1

print(f"  Sum of values before sentinel (-1): {total}")


# 6. Common Use Case: Validating Input
print("\n--- Input Validation Pattern ---")
# Simulating repeated prompts until valid input is given
attempts = ["", "abc", "42"]  # Simulated user responses
attempt_index = 0

while attempt_index < len(attempts):
    response = attempts[attempt_index]
    attempt_index += 1

    if not response:
        print("  Empty input, try again...")
        continue
    if not response.isdigit():
        print(f"  '{response}' is not a number, try again...")
        continue

    print(f"  Valid number entered: {response}")
    break


# 7. Avoiding Infinite Loops
print("\n--- Avoiding Infinite Loops ---")
print("  Common causes of infinite loops:")
print("    1. Forgetting to update the loop variable (e.g., missing 'count += 1')")
print("    2. Condition that can never become False")
print("    3. Accidentally resetting the loop variable inside the loop")
print("  Tip: Always have a clear exit strategy (update variable, break, or max iterations).")

# Safety pattern: Max iterations
MAX_ITERATIONS = 1000
i = 0
while i < MAX_ITERATIONS:
    # ... do work ...
    if i == 5:  # Some exit condition
        break
    i += 1
print(f"  Safe loop exited at iteration {i}")


# 8. While vs For - When to Use Which
print("\n--- While vs For ---")
print("  Use FOR when:")
print("    - You know the number of iterations in advance")
print("    - You're iterating over a collection (list, dict, string)")
print("  Use WHILE when:")
print("    - You DON'T know when to stop (depends on a condition)")
print("    - You need an event loop or are waiting for user input")
print("    - You need a loop that might not execute at all")
