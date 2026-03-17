"""
Python Collections Module - Specialized Container Data Types
"""
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

# ============================================================
# 1. Counter — Count occurrences of elements
# ============================================================
print("--- Counter ---")

words = "how many times does each word show up in this sentence with each word".split()
word_count = Counter(words)
print(f"  Counter: {word_count}")
print(f"  Most common 3: {word_count.most_common(3)}")

letters = Counter("mississippi")
print(f"  Letters in 'mississippi': {letters}")
print(f"  's' count: {letters['s']}")

# Counter arithmetic
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"  {c1} + {c2} = {c1 + c2}")
print(f"  {c1} - {c2} = {c1 - c2}")  # Only keeps positive counts


# ============================================================
# 2. defaultdict — Dictionary with default values
# ============================================================
print("\n--- defaultdict ---")

# Normal dict raises KeyError for missing keys
# defaultdict returns a default value instead

d = defaultdict(int)  # Default value is 0
for word in "hello world hello python hello".split():
    d[word] += 1
print(f"  Word counts: {dict(d)}")

d2 = defaultdict(list)  # Default value is empty list
pairs = [("fruit", "apple"), ("fruit", "banana"), ("veggie", "carrot"), ("fruit", "cherry")]
for category, item in pairs:
    d2[category].append(item)
print(f"  Grouped: {dict(d2)}")

d3 = defaultdict(lambda: "Unknown")
d3["name"] = "Alice"
print(f"  d3['name'] = {d3['name']}")
print(f"  d3['age'] = {d3['age']}")  # Returns "Unknown" instead of KeyError


# ============================================================
# 3. OrderedDict — Remembers insertion order (Python 3.7+: regular dicts do too)
# ============================================================
print("\n--- OrderedDict ---")

od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3
print(f"  OrderedDict: {od}")

# Useful for: move_to_end() and equality that considers order
od.move_to_end("first")
print(f"  After move_to_end('first'): {od}")

# Regular dicts consider order for ==, OrderedDict also does
d1 = OrderedDict([("a", 1), ("b", 2)])
d2 = OrderedDict([("b", 2), ("a", 1)])
print(f"  Order matters: d1 == d2? {d1 == d2}")  # False


# ============================================================
# 4. namedtuple — Lightweight, immutable objects
# ============================================================
print("\n--- namedtuple ---")

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"  Point: {p}")
print(f"  p.x={p.x}, p.y={p.y}")
print(f"  p[0]={p[0]}, p[1]={p[1]}")  # Also indexable

# Great for representing structured data without a full class
Color = namedtuple("Color", "red green blue")
white = Color(255, 255, 255)
print(f"  White: {white}")

# Convert to dict
print(f"  As dict: {p._asdict()}")


# ============================================================
# 5. deque — Double-ended queue (fast appends/pops from both ends)
# ============================================================
print("\n--- deque ---")

dq = deque([1, 2, 3])
dq.append(4)        # Add to right
dq.appendleft(0)    # Add to left
print(f"  After appends: {dq}")

dq.pop()             # Remove from right
dq.popleft()         # Remove from left
print(f"  After pops: {dq}")

dq.extend([4, 5])
dq.extendleft([-1, -2])  # Note: extends in reverse order
print(f"  After extends: {dq}")

dq.rotate(2)         # Rotate right by 2
print(f"  After rotate(2): {dq}")

# Fixed-size deque — automatically drops oldest items
recent = deque(maxlen=3)
for i in range(5):
    recent.append(i)
    print(f"    Added {i}: {list(recent)}")
