"""
Timing Your Python Code - Measuring Performance
"""
import time
import timeit

# ============================================================
# 1. time.time() — Simple Wall-Clock Timing
# ============================================================
print("--- time.time() ---")

start = time.time()
# Code to measure
total = sum(range(1_000_000))
end = time.time()

elapsed = end - start
print(f"  Sum of 0..999,999 = {total}")
print(f"  Elapsed: {elapsed:.6f} seconds")


# ============================================================
# 2. time.perf_counter() — High-Resolution Timer (Recommended)
# ============================================================
print("\n--- time.perf_counter() ---")

start = time.perf_counter()
total = sum(range(1_000_000))
end = time.perf_counter()

print(f"  Elapsed: {end - start:.6f} seconds (higher precision)")


# ============================================================
# 3. timeit Module — Reliable Benchmarking
# ============================================================
print("\n--- timeit Module ---")

# timeit runs the code many times and gives you the average
# This avoids noise from OS scheduling, caching, etc.

# Method 1: timeit.timeit() with a string
t1 = timeit.timeit("sum(range(1000))", number=10_000)
print(f"  sum(range(1000)) x10,000: {t1:.4f}s")

# Method 2: timeit.timeit() with a function
def test_function():
    return [x**2 for x in range(100)]

t2 = timeit.timeit(test_function, number=10_000)
print(f"  List comprehension x10,000: {t2:.4f}s")


# ============================================================
# 4. Comparing Different Approaches
# ============================================================
print("\n--- Comparing Approaches ---")

# For loop vs list comprehension vs map
n = 10_000

t_for = timeit.timeit("""
result = []
for x in range(100):
    result.append(x**2)
""", number=n)

t_comp = timeit.timeit("[x**2 for x in range(100)]", number=n)

t_map = timeit.timeit("list(map(lambda x: x**2, range(100)))", number=n)

print(f"  For loop:           {t_for:.4f}s")
print(f"  List comprehension: {t_comp:.4f}s")
print(f"  map + lambda:       {t_map:.4f}s")

fastest = min(t_for, t_comp, t_map)
print(f"  Winner: {'For loop' if fastest == t_for else 'Comprehension' if fastest == t_comp else 'Map'}")


# ============================================================
# 5. String Concatenation Comparison
# ============================================================
print("\n--- String Concatenation ---")
n = 5_000

t_plus = timeit.timeit("""
s = ""
for i in range(100):
    s += str(i)
""", number=n)

t_join = timeit.timeit("""
s = "".join(str(i) for i in range(100))
""", number=n)

t_fstring = timeit.timeit("""
parts = [f"{i}" for i in range(100)]
s = "".join(parts)
""", number=n)

print(f"  += concatenation:  {t_plus:.4f}s")
print(f"  ''.join():         {t_join:.4f}s")
print(f"  f-string + join:   {t_fstring:.4f}s")


# ============================================================
# 6. Creating a Timer Decorator
# ============================================================
print("\n--- Timer Decorator ---")

def timer(func):
    """Decorator that measures how long a function takes."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__}() took {elapsed:.6f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

@timer
def fast_sum(n):
    return n * (n - 1) // 2

slow_sum(1_000_000)
fast_sum(1_000_000)
