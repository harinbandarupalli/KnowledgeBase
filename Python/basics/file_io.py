"""
Python File I/O - Reading, Writing, and Working with Files
"""
import os

# We will use a temporary file for demonstration
FILE_PATH = "sample_output.txt"

# 1. Writing to a File
# Mode 'w' creates a new file or OVERWRITES an existing one.
print("--- Writing to a File ('w' mode) ---")
with open(FILE_PATH, "w") as f:
    f.write("Hello, this is line 1.\n")
    f.write("This is line 2.\n")
    f.write("And this is line 3.\n")
print(f"Successfully wrote to '{FILE_PATH}'")


# 2. Reading an Entire File
print("\n--- Reading Entire File ('r' mode) ---")
with open(FILE_PATH, "r") as f:
    content = f.read()
print(content)


# 3. Reading Line by Line
print("--- Reading Line by Line ---")
with open(FILE_PATH, "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"  Line {line_number}: {line.strip()}")  # .strip() removes trailing newline


# 4. Reading All Lines into a List
print("\n--- Reading All Lines into a List ---")
with open(FILE_PATH, "r") as f:
    lines = f.readlines()
print(f"Lines as list: {lines}")


# 5. Appending to a File
# Mode 'a' adds content to the END of an existing file (does not overwrite).
print("\n--- Appending to a File ('a' mode) ---")
with open(FILE_PATH, "a") as f:
    f.write("This line was appended!\n")

with open(FILE_PATH, "r") as f:
    print(f.read())


# 6. The `with` Statement (Context Manager)
print("--- Why use 'with' ---")
print("The 'with' statement automatically closes the file after the block finishes,")
print("even if an error occurs. This prevents resource leaks.")
print("Without 'with', you would need to manually call f.close().")


# 7. File Modes Summary
print("\n--- File Modes Summary ---")
modes = {
    "'r'": "Read only (default). Error if file doesn't exist.",
    "'w'": "Write only. Creates new or OVERWRITES existing file.",
    "'a'": "Append only. Creates new or appends to existing file.",
    "'r+'": "Read and Write. Error if file doesn't exist.",
    "'rb'": "Read binary (for images, PDFs, etc.).",
    "'wb'": "Write binary.",
}
for mode, description in modes.items():
    print(f"  {mode:6} -> {description}")


# 8. Checking if a File Exists
print("\n--- Checking File Existence ---")
print(f"Does '{FILE_PATH}' exist? {os.path.exists(FILE_PATH)}")
print(f"Is it a file? {os.path.isfile(FILE_PATH)}")
print(f"Is it a directory? {os.path.isdir(FILE_PATH)}")


# 9. Working with File Paths
print("\n--- Working with File Paths ---")
full_path = os.path.abspath(FILE_PATH)
print(f"Absolute Path: {full_path}")
print(f"Directory Name: {os.path.dirname(full_path)}")
print(f"File Name: {os.path.basename(full_path)}")
print(f"File Extension: {os.path.splitext(full_path)[1]}")


# 10. Cleanup - Remove the demo file
os.remove(FILE_PATH)
print(f"\nCleaned up: Removed '{FILE_PATH}'")
