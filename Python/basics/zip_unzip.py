"""
Zipping and Unzipping Files with Python
"""
import zipfile
import os
import shutil

# ============================================================
# 1. Creating a Zip File
# ============================================================
print("--- Creating a Zip File ---")

# Create some demo files first
os.makedirs("zip_demo", exist_ok=True)
for i in range(3):
    with open(f"zip_demo/file_{i}.txt", "w") as f:
        f.write(f"This is the content of file {i}.\n" * 5)

# Create a zip archive
with zipfile.ZipFile("demo_archive.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    for filename in os.listdir("zip_demo"):
        filepath = os.path.join("zip_demo", filename)
        zf.write(filepath)
        print(f"  Added: {filepath}")

print("  Created demo_archive.zip")


# ============================================================
# 2. Listing Contents of a Zip File
# ============================================================
print("\n--- Listing Zip Contents ---")

with zipfile.ZipFile("demo_archive.zip", "r") as zf:
    print(f"  Files in archive: {zf.namelist()}")
    for info in zf.infolist():
        print(f"    {info.filename}: {info.file_size} bytes "
              f"-> {info.compress_size} bytes compressed")


# ============================================================
# 3. Extracting a Zip File
# ============================================================
print("\n--- Extracting ---")

# Extract ALL files
with zipfile.ZipFile("demo_archive.zip", "r") as zf:
    zf.extractall("extracted_demo")
    print(f"  Extracted all to 'extracted_demo/'")
    print(f"  Contents: {os.listdir('extracted_demo')}")

# Extract a SINGLE file
with zipfile.ZipFile("demo_archive.zip", "r") as zf:
    zf.extract("zip_demo/file_0.txt", "single_extract")
    print(f"  Extracted single file to 'single_extract/'")


# ============================================================
# 4. Reading Files Directly from a Zip (Without Extracting)
# ============================================================
print("\n--- Reading Without Extracting ---")

with zipfile.ZipFile("demo_archive.zip", "r") as zf:
    with zf.open("zip_demo/file_0.txt") as f:
        content = f.read().decode("utf-8")
        print(f"  First line: {content.splitlines()[0]}")


# ============================================================
# 5. Adding Files to an Existing Zip
# ============================================================
print("\n--- Appending to Zip ---")

with open("zip_demo/extra_file.txt", "w") as f:
    f.write("This file was added later!")

with zipfile.ZipFile("demo_archive.zip", "a") as zf:  # 'a' for append
    zf.write("zip_demo/extra_file.txt")
    print(f"  Appended extra_file.txt")
    print(f"  Updated contents: {zf.namelist()}")


# ============================================================
# 6. shutil — Quick Archive Creation
# ============================================================
print("\n--- shutil.make_archive() ---")

# shutil can create zip, tar, gzip, bzip2 archives in one line
shutil.make_archive("shutil_demo", "zip", "zip_demo")
print("  Created shutil_demo.zip from zip_demo/ folder")


# ============================================================
# 7. Cleanup
# ============================================================
print("\n--- Cleanup ---")
# Remove demo files
shutil.rmtree("zip_demo", ignore_errors=True)
shutil.rmtree("extracted_demo", ignore_errors=True)
shutil.rmtree("single_extract", ignore_errors=True)
for f in ["demo_archive.zip", "shutil_demo.zip"]:
    if os.path.exists(f):
        os.remove(f)
print("  All demo files cleaned up!")
