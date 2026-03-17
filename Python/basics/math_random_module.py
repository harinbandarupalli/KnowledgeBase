"""
Python Math and Random Modules
"""
import math
import random

# ============================================================
# 1. Math Module — Mathematical Functions and Constants
# ============================================================
print("--- Math Constants ---")
print(f"  math.pi:  {math.pi}")
print(f"  math.e:   {math.e}")
print(f"  math.tau: {math.tau}")  # 2 * pi
print(f"  math.inf: {math.inf}")
print(f"  math.nan: {math.nan}")

print("\n--- Rounding ---")
print(f"  math.floor(4.7):  {math.floor(4.7)}")   # 4 (round down)
print(f"  math.ceil(4.2):   {math.ceil(4.2)}")     # 5 (round up)
print(f"  math.trunc(4.9):  {math.trunc(4.9)}")    # 4 (truncate decimal)
print(f"  round(4.5):       {round(4.5)}")          # 4 (banker's rounding)
print(f"  round(5.5):       {round(5.5)}")          # 6 (banker's rounding)

print("\n--- Powers and Roots ---")
print(f"  math.sqrt(144):   {math.sqrt(144)}")
print(f"  math.pow(2, 10):  {math.pow(2, 10)}")
print(f"  math.log(100, 10): {math.log(100, 10)}")  # log base 10
print(f"  math.log2(1024):  {math.log2(1024)}")
print(f"  math.log10(1000): {math.log10(1000)}")
print(f"  math.exp(1):      {math.exp(1)}")          # e^1

print("\n--- Trigonometry ---")
print(f"  math.sin(pi/2):  {math.sin(math.pi / 2):.4f}")
print(f"  math.cos(0):     {math.cos(0):.4f}")
print(f"  math.radians(180): {math.radians(180):.4f}")
print(f"  math.degrees(pi):  {math.degrees(math.pi):.4f}")

print("\n--- Other Useful Functions ---")
print(f"  math.factorial(5):  {math.factorial(5)}")   # 120
print(f"  math.gcd(12, 8):    {math.gcd(12, 8)}")     # 4
print(f"  math.comb(10, 3):   {math.comb(10, 3)}")    # 120 (10 choose 3)
print(f"  math.perm(5, 2):    {math.perm(5, 2)}")     # 20
print(f"  math.fabs(-42.5):   {math.fabs(-42.5)}")
print(f"  math.isfinite(42):  {math.isfinite(42)}")
print(f"  math.isinf(math.inf): {math.isinf(math.inf)}")


# ============================================================
# 2. Random Module — Random Number Generation
# ============================================================
print("\n--- Random Numbers ---")

# Set seed for reproducibility (same "random" numbers each time)
random.seed(42)

print(f"  random.random():       {random.random():.4f}")         # Float [0.0, 1.0)
print(f"  random.uniform(1, 10): {random.uniform(1, 10):.4f}")  # Float [1, 10]
print(f"  random.randint(1, 100): {random.randint(1, 100)}")    # Int [1, 100]
print(f"  random.randrange(0, 100, 5): {random.randrange(0, 100, 5)}")  # Step of 5

print("\n--- Random Choices ---")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(f"  random.choice(fruits):  {random.choice(fruits)}")
print(f"  random.choices(fruits, k=3): {random.choices(fruits, k=3)}")  # With replacement
print(f"  random.sample(fruits, k=3):  {random.sample(fruits, k=3)}")   # Without replacement

print("\n--- Shuffling ---")
deck = list(range(1, 11))
print(f"  Before shuffle: {deck}")
random.shuffle(deck)  # In-place
print(f"  After shuffle:  {deck}")

print("\n--- Random with Weights ---")
# Weighted random choices (e.g., loot drops in a game)
items = ["common", "rare", "legendary"]
weights = [70, 25, 5]
drops = random.choices(items, weights=weights, k=10)
print(f"  10 loot drops: {drops}")

print("\n--- Gaussian (Normal) Distribution ---")
values = [random.gauss(mu=100, sigma=15) for _ in range(5)]
print(f"  5 samples (mean=100, std=15): {[f'{v:.1f}' for v in values]}")
