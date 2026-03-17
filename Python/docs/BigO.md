# Big O Notation for Python Data Structures

Big O notation describes the **worst-case time complexity** of an operation — how its performance scales as the input size (`n`) grows.

> [!TIP]
> **Quick Reference:** O(1) is instant, O(n) is linear (scans everything), O(n²) is slow for large data.

---

## 📋 Lists (`list`)

Lists are implemented as **dynamic arrays** in CPython.

| Operation | Average Case | Worst Case | Notes |
|---|---|---|---|
| Index `l[i]` | O(1) | O(1) | Direct memory access |
| Store `l[i] = val` | O(1) | O(1) | Direct memory access |
| Append `l.append(val)` | O(1) | O(1) | Amortized; occasional resize is O(n) |
| Pop last `l.pop()` | O(1) | O(1) | |
| Pop intermediate `l.pop(i)` | O(n) | O(n) | Shifts all elements after index `i` |
| Insert `l.insert(i, val)` | O(n) | O(n) | Shifts all elements after index `i` |
| Delete `del l[i]` | O(n) | O(n) | Shifts all elements after index `i` |
| Containment `x in l` | O(n) | O(n) | Must scan the entire list |
| Length `len(l)` | O(1) | O(1) | Stored as attribute |
| Slice `l[a:b]` | O(b-a) | O(b-a) | Copies the slice |
| Extend `l.extend(k)` | O(len(k)) | O(len(k)) | |
| Sort `l.sort()` | O(n log n) | O(n log n) | Timsort |
| Min/Max `min(l)` / `max(l)` | O(n) | O(n) | Must scan everything |
| Reverse `l.reverse()` | O(n) | O(n) | |
| List Comprehension | O(n) | O(n) | Iterates through all elements |

> **Takeaway:** Lists are great for **indexed access** and **appending**. Avoid frequent inserts/deletes at the beginning or middle for large lists.

---

## 📖 Dictionaries (`dict`)

Dictionaries are implemented as **hash tables** in CPython.

| Operation | Average Case | Worst Case | Notes |
|---|---|---|---|
| Get `d[key]` | O(1) | O(n) | O(n) only with extreme hash collisions (rare) |
| Set `d[key] = val` | O(1) | O(n) | Amortized O(1) |
| Delete `del d[key]` | O(1) | O(n) | |
| Containment `key in d` | O(1) | O(n) | Hash lookup |
| Length `len(d)` | O(1) | O(1) | |
| Get keys `d.keys()` | O(1) | O(1) | Returns a view object |
| Get values `d.values()` | O(1) | O(1) | Returns a view object |
| Iteration | O(n) | O(n) | Iterates over all key-value pairs |

> **Takeaway:** Dictionaries provide **near-instant lookups** by key. If you need to frequently check whether something exists, a dictionary (or set) is far better than a list.

---

## 📦 Tuples (`tuple`)

Tuples are implemented as **immutable fixed-size arrays**.

| Operation | Average Case | Worst Case | Notes |
|---|---|---|---|
| Index `t[i]` | O(1) | O(1) | Direct memory access |
| Containment `x in t` | O(n) | O(n) | Must scan the sequence |
| Length `len(t)` | O(1) | O(1) | |
| Slice `t[a:b]` | O(b-a) | O(b-a) | Creates a new tuple |
| Min/Max | O(n) | O(n) | |

> **Takeaway:** Tuples have the same lookup speed as lists but are **slightly faster to create** and use less memory due to immutability. They cannot be modified, so there are no insert/delete operations.

---

## 🔗 Sets (`set`)

Sets are implemented as **hash tables** (like dictionaries, but only keys — no values).

| Operation | Average Case | Worst Case | Notes |
|---|---|---|---|
| Add `s.add(val)` | O(1) | O(n) | Amortized O(1) |
| Remove `s.remove(val)` | O(1) | O(n) | |
| Discard `s.discard(val)` | O(1) | O(n) | Same as remove but no error if missing |
| Containment `x in s` | O(1) | O(n) | Hash lookup |
| Length `len(s)` | O(1) | O(1) | |
| Union `s \| t` | O(len(s) + len(t)) | | |
| Intersection `s & t` | O(min(len(s), len(t))) | | |
| Difference `s - t` | O(len(s)) | | |
| Symmetric Diff `s ^ t` | O(len(s) + len(t)) | | |
| Is Subset `s <= t` | O(len(s)) | | |
| Pop `s.pop()` | O(1) | O(1) | Removes an arbitrary element |

> **Takeaway:** Sets give you **O(1) membership testing** (`in`). If your primary need is checking whether an item exists, always prefer a set over a list.

---

## ⚡ Quick Comparison: When to Use What

| Need | Best Structure | Why |
|---|---|---|
| Ordered collection, fast append | `list` | O(1) append, O(1) index |
| Fast key-based lookup | `dict` | O(1) get/set by key |
| Immutable ordered data | `tuple` | Faster creation, hashable |
| Unique items, fast membership check | `set` | O(1) `in` check |
| Check if item exists in collection | `set` or `dict` | O(1) vs O(n) for list |

---

## 🔗 Further Reading
- [Python Wiki: Time Complexity](https://wiki.python.org/moin/TimeComplexity) — Official CPython complexity guarantees
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/) — Visual reference for all common data structures and algorithms
