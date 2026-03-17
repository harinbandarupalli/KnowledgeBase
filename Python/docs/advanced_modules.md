# Advanced Python Modules Guide

This document covers Python's most useful built-in modules for working with data, files, dates, debugging, and more.

---

## Scripts

| # | Module | File |
|---|--------|------|
| 1 | Collections | [collections_module.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/collections_module.py) |
| 2 | OS & File System | [os_module.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/os_module.py) |
| 3 | Datetime | [datetime_module.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/datetime_module.py) |
| 4 | Math & Random | [math_random_module.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/math_random_module.py) |
| 5 | Debugger (pdb) | [debugger_pdb.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/debugger_pdb.py) |
| 6 | Regular Expressions | [regex_module.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/regex_module.py) |
| 7 | Timing Code | [timing_code.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/timing_code.py) |
| 8 | Zip/Unzip Files | [zip_unzip.py](file:///c:/Users/harik/Documents/projects/KnowledgeBase/Python/basics/zip_unzip.py) |

---

## 1. Collections Module
`from collections import Counter, defaultdict, OrderedDict, namedtuple, deque`

| Class | Purpose |
|-------|---------|
| `Counter` | Count occurrences — `Counter("mississippi")` → `{'s': 4, 'i': 4, ...}` |
| `defaultdict` | Dict with default values — never raises `KeyError` |
| `OrderedDict` | Dict with `move_to_end()` and order-sensitive equality |
| `namedtuple` | Lightweight immutable objects — `Point(x=3, y=4)` |
| `deque` | Fast appends/pops from both ends; fixed-size with `maxlen` |

---

## 2. OS Module — File System Operations
`import os, shutil`

| Function | Purpose |
|----------|---------|
| `os.getcwd()` | Current working directory |
| `os.listdir(path)` | List directory contents |
| `os.path.join()` | Join paths (cross-platform) |
| `os.path.exists()` | Check if file/dir exists |
| `os.walk(path)` | Walk entire directory tree |
| `os.makedirs()` | Create nested directories |
| `os.rename()` | Rename file/directory |
| `os.remove()` | Delete a file |
| `shutil.copy()` | Copy a file |
| `shutil.rmtree()` | Delete a directory tree |

---

## 3. Datetime Module
`from datetime import datetime, date, time, timedelta`

**Key Operations:**
- **Current time:** `datetime.now()`, `date.today()`
- **Formatting:** `dt.strftime("%Y-%m-%d %H:%M")` (date → string)
- **Parsing:** `datetime.strptime("Dec 25, 2025", "%B %d, %Y")` (string → date)
- **Arithmetic:** `date.today() + timedelta(days=30)`
- **Comparison:** `date1 < date2`

Common format codes: `%Y`(year), `%m`(month), `%d`(day), `%H`(24h), `%I`(12h), `%M`(min), `%S`(sec), `%A`(weekday), `%B`(month name)

---

## 4. Math & Random Modules

**Math** — `import math`
- Constants: `math.pi`, `math.e`, `math.inf`
- Rounding: `floor()`, `ceil()`, `trunc()`
- Powers: `sqrt()`, `pow()`, `log()`, `exp()`
- Factorials: `factorial()`, `comb()`, `perm()`, `gcd()`

**Random** — `import random`
- Numbers: `random()`, `uniform()`, `randint()`, `gauss()`
- Choices: `choice()`, `choices(weights=...)`, `sample()`
- Shuffle: `shuffle()` (in-place)
- Seed: `random.seed(42)` for reproducibility

---

## 5. Python Debugger (pdb)

| Command | Action |
|---------|--------|
| `n` (next) | Execute next line (step over) |
| `s` (step) | Step into function |
| `c` (continue) | Continue to next breakpoint |
| `p expr` | Print value of expression |
| `l` (list) | Show source code |
| `b line` | Set breakpoint at line |
| `q` (quit) | Quit debugger |

**Usage:** Add `breakpoint()` in your code (Python 3.7+), or run `python -m pdb script.py`

---

## 6. Regular Expressions (re)
`import re`

| Function | Purpose |
|----------|---------|
| `re.search(pattern, text)` | Find first match anywhere |
| `re.match(pattern, text)` | Match at start only |
| `re.findall(pattern, text)` | Find all matches (list) |
| `re.sub(pattern, repl, text)` | Find and replace |
| `re.split(pattern, text)` | Split on pattern |
| `re.compile(pattern)` | Pre-compile for reuse |

**Common patterns:** `\d` (digit), `\w` (word char), `\s` (whitespace), `.` (any), `+` (1+), `*` (0+), `?` (0 or 1), `{n}` (exactly n), `()` groups

---

## 7. Timing Your Code

| Method | Best For |
|--------|----------|
| `time.perf_counter()` | Simple one-off timing |
| `timeit.timeit(code, number=N)` | Reliable benchmarks (averages over N runs) |
| `@timer` decorator | Automatic timing of function calls |

---

## 8. Zipping & Unzipping Files
`import zipfile, shutil`

```python
# Create
with zipfile.ZipFile("archive.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write("myfile.txt")

# Extract
with zipfile.ZipFile("archive.zip", "r") as zf:
    zf.extractall("output_dir")

# Quick archive with shutil
shutil.make_archive("backup", "zip", "my_folder")
```
