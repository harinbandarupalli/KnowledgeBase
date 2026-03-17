"""
Python Regular Expressions (re module) - Pattern Matching
"""
import re

# ============================================================
# 1. Basic Pattern Matching
# ============================================================
print("--- Basic Matching ---")

text = "The phone number is 415-555-1234"

# re.search() — find first match anywhere in the string
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print(f"  Found: {match.group()}")
    print(f"  Span:  {match.span()}")

# re.match() — only matches at the BEGINNING of the string
match2 = re.match(r"The", text)
print(f"  re.match('The'): {match2.group() if match2 else 'No match'}")

match3 = re.match(r"phone", text)
print(f"  re.match('phone'): {match3 if match3 else 'No match (not at start)'}")


# ============================================================
# 2. Common Regex Patterns
# ============================================================
print("\n--- Common Patterns ---")
patterns = {
    r"\d":    "Any digit (0-9)",
    r"\D":    "Any non-digit",
    r"\w":    "Any word char (letter, digit, underscore)",
    r"\W":    "Any non-word char",
    r"\s":    "Any whitespace (space, tab, newline)",
    r"\S":    "Any non-whitespace",
    r".":     "Any character except newline",
    r"^":     "Start of string",
    r"$":     "End of string",
}
for pattern, desc in patterns.items():
    print(f"  {pattern:8} -> {desc}")


# ============================================================
# 3. Quantifiers
# ============================================================
print("\n--- Quantifiers ---")
quantifiers = {
    r"a*":     "Zero or more 'a'",
    r"a+":     "One or more 'a'",
    r"a?":     "Zero or one 'a'",
    r"a{3}":   "Exactly 3 'a's",
    r"a{2,4}": "Between 2 and 4 'a's",
    r"a{2,}":  "2 or more 'a's",
}
for q, desc in quantifiers.items():
    print(f"  {q:10} -> {desc}")

# Greedy vs Non-Greedy
html = "<h1>Title</h1>"
greedy = re.search(r"<.*>", html)
non_greedy = re.search(r"<.*?>", html)
print(f"\n  Greedy   '<.*>':  {greedy.group()}")
print(f"  Non-greedy '<.*?>': {non_greedy.group()}")


# ============================================================
# 4. Groups — Extracting Parts of a Match
# ============================================================
print("\n--- Groups ---")

text = "John Smith, Age: 30, Email: john@example.com"

# Parentheses create groups
match = re.search(r"(\w+) (\w+), Age: (\d+)", text)
if match:
    print(f"  Full match: {match.group()}")
    print(f"  Group 1 (first name): {match.group(1)}")
    print(f"  Group 2 (last name):  {match.group(2)}")
    print(f"  Group 3 (age):        {match.group(3)}")
    print(f"  All groups: {match.groups()}")


# Named groups
match = re.search(r"(?P<first>\w+) (?P<last>\w+), Age: (?P<age>\d+)", text)
if match:
    print(f"  Named group 'first': {match.group('first')}")
    print(f"  Named group 'last':  {match.group('last')}")
    print(f"  groupdict(): {match.groupdict()}")


# ============================================================
# 5. findall() and finditer()
# ============================================================
print("\n--- findall() and finditer() ---")

text = "Call 415-555-1234 or 800-555-9999 or 212-555-0000"

# findall returns a list of ALL matches
phones = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(f"  All phones: {phones}")

# finditer returns an iterator of match objects (with position info)
for m in re.finditer(r"\d{3}-\d{3}-\d{4}", text):
    print(f"  Found {m.group()} at position {m.span()}")

# findall with groups returns the groups, not the full match
emails_text = "Contact alice@gmail.com and bob@company.org"
emails = re.findall(r"(\w+)@(\w+\.\w+)", emails_text)
print(f"  Email parts: {emails}")


# ============================================================
# 6. sub() and split() — Replace and Split
# ============================================================
print("\n--- sub() and split() ---")

# Replace patterns
text = "My phone is 415-555-1234"
censored = re.sub(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", text)
print(f"  Censored: {censored}")

# Replace with a function
def censor_partial(match):
    return match.group()[:3] + "-XXX-XXXX"
partial = re.sub(r"\d{3}-\d{3}-\d{4}", censor_partial, text)
print(f"  Partial censor: {partial}")

# Split on pattern
text = "one,  two;  three   four"
parts = re.split(r"[,;\s]+", text)
print(f"  Split: {parts}")


# ============================================================
# 7. Character Classes and OR
# ============================================================
print("\n--- Character Classes ---")

# [abc]   — matches a, b, or c
# [a-z]   — matches any lowercase letter
# [^abc]  — matches anything EXCEPT a, b, or c
# a|b     — matches a OR b

text = "cat bat hat rat mat"
matches = re.findall(r"[cbh]at", text)
print(f"  [cbh]at: {matches}")

matches2 = re.findall(r"[^r ]at", text)
print(f"  [^r ]at (not rat): {matches2}")

# OR operator
matches3 = re.findall(r"cat|dog", "I have a cat and a dog")
print(f"  cat|dog: {matches3}")


# ============================================================
# 8. Compile for Reuse
# ============================================================
print("\n--- Compiled Patterns ---")

# Compile a pattern for repeated use (faster)
email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")

texts = [
    "Email me at alice@gmail.com",
    "Contact bob.smith@company.co.uk",
    "No email here!",
]
for t in texts:
    found = email_pattern.findall(t)
    print(f"  '{t[:30]}...' -> {found}")


# ============================================================
# 9. Common Real-World Patterns
# ============================================================
print("\n--- Useful Patterns ---")
useful = {
    r"[\w.+-]+@[\w-]+\.[\w.-]+":          "Email address",
    r"\d{3}[-.\s]?\d{3}[-.\s]?\d{4}":    "US phone number",
    r"https?://[\w./\-?=&]+":            "URL",
    r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b": "IP address",
    r"^\d{5}(-\d{4})?$":                  "US zip code",
}
for pattern, desc in useful.items():
    print(f"  {desc:20} -> {pattern}")
