"""
Python OS Module - File System Navigation, File/Folder Operations
"""
import os
import shutil

# ============================================================
# 1. Getting Current Directory and Listing Contents
# ============================================================
print("--- Current Directory & Listing ---")

cwd = os.getcwd()
print(f"  Current directory: {cwd}")

# List files and folders in a directory
print(f"  Contents of cwd: {os.listdir('.')[:10]}...")  # First 10 items

# Check if something is a file or directory
for item in os.listdir('.')[:5]:
    item_type = "DIR " if os.path.isdir(item) else "FILE"
    print(f"    {item_type}: {item}")


# ============================================================
# 2. Path Operations with os.path
# ============================================================
print("\n--- os.path Operations ---")

# Join paths (OS-independent)
full_path = os.path.join("folder", "subfolder", "file.txt")
print(f"  os.path.join: {full_path}")

# Split path into components
print(f"  dirname:  {os.path.dirname('/home/user/file.txt')}")
print(f"  basename: {os.path.basename('/home/user/file.txt')}")
print(f"  split:    {os.path.split('/home/user/file.txt')}")
print(f"  splitext: {os.path.splitext('document.tar.gz')}")

# Absolute path
print(f"  abspath('.'): {os.path.abspath('.')}")

# Check existence
print(f"  exists('.'): {os.path.exists('.')}")
print(f"  isfile('.'): {os.path.isfile('.')}")
print(f"  isdir('.'):  {os.path.isdir('.')}")


# ============================================================
# 3. Walking a Directory Tree
# ============================================================
print("\n--- os.walk() ---")
print("  os.walk() yields (dirpath, dirnames, filenames) for each directory:")

# Walk current directory (limited output for demo)
count = 0
for dirpath, dirnames, filenames in os.walk('.'):
    print(f"  📁 {dirpath}")
    print(f"     Subdirs:  {dirnames[:3]}")
    print(f"     Files:    {filenames[:3]}")
    count += 1
    if count >= 3:  # Limit output
        print("     ... (truncated)")
        break


# ============================================================
# 4. Creating and Removing Directories
# ============================================================
print("\n--- Creating & Removing Directories ---")

# Create a single directory
if not os.path.exists("temp_demo"):
    os.mkdir("temp_demo")
    print("  Created 'temp_demo'")

# Create nested directories (like mkdir -p)
os.makedirs("temp_demo/sub1/sub2", exist_ok=True)
print("  Created 'temp_demo/sub1/sub2'")

# Remove directory (must be empty)
# os.rmdir("temp_demo/sub1/sub2")

# Remove directory tree (including contents)
if os.path.exists("temp_demo"):
    shutil.rmtree("temp_demo")
    print("  Removed 'temp_demo' and all contents")


# ============================================================
# 5. File Operations
# ============================================================
print("\n--- File Operations ---")

# Create a temp file for demo
with open("temp_os_demo.txt", "w") as f:
    f.write("Hello from OS module demo!")

# Get file info
file_path = "temp_os_demo.txt"
print(f"  File size: {os.path.getsize(file_path)} bytes")

stat = os.stat(file_path)
print(f"  File stat: size={stat.st_size}, modified={stat.st_mtime}")

# Rename a file
os.rename("temp_os_demo.txt", "temp_os_renamed.txt")
print("  Renamed temp_os_demo.txt -> temp_os_renamed.txt")

# Copy a file (using shutil)
shutil.copy("temp_os_renamed.txt", "temp_os_copy.txt")
print("  Copied to temp_os_copy.txt")

# Move a file
# shutil.move("temp_os_copy.txt", "some_other_dir/temp_os_copy.txt")

# Delete files
os.remove("temp_os_renamed.txt")
os.remove("temp_os_copy.txt")
print("  Cleaned up temp files")


# ============================================================
# 6. Environment Variables
# ============================================================
print("\n--- Environment Variables ---")
print(f"  PATH (first 80 chars): {os.environ.get('PATH', 'N/A')[:80]}...")
print(f"  HOME: {os.environ.get('HOME', os.environ.get('USERPROFILE', 'N/A'))}")
print(f"  Custom var: {os.environ.get('MY_CUSTOM_VAR', 'Not set')}")
