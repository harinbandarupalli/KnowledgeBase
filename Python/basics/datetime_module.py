"""
Python Datetime Module - Working with Dates and Times
"""
from datetime import datetime, date, time, timedelta
import calendar

# ============================================================
# 1. Current Date and Time
# ============================================================
print("--- Current Date & Time ---")

now = datetime.now()
print(f"  datetime.now():  {now}")
print(f"  date.today():    {date.today()}")
print(f"  Year:  {now.year}")
print(f"  Month: {now.month}")
print(f"  Day:   {now.day}")
print(f"  Hour:  {now.hour}")
print(f"  Min:   {now.minute}")
print(f"  Sec:   {now.second}")
print(f"  Weekday: {now.strftime('%A')}")


# ============================================================
# 2. Creating Specific Dates and Times
# ============================================================
print("\n--- Creating Dates ---")

birthday = date(1990, 5, 15)
print(f"  Birthday: {birthday}")

meeting = datetime(2025, 12, 25, 14, 30, 0)
print(f"  Meeting: {meeting}")

t = time(14, 30, 45)
print(f"  Time: {t}")


# ============================================================
# 3. Formatting Dates (strftime)
# ============================================================
print("\n--- strftime (Date -> String) ---")

now = datetime.now()
formats = {
    "%Y-%m-%d":          "ISO format",
    "%d/%m/%Y":          "Day/Month/Year",
    "%B %d, %Y":         "Full month name",
    "%b %d, %Y":         "Abbreviated month",
    "%A, %B %d, %Y":     "Full weekday + date",
    "%I:%M %p":          "12-hour time",
    "%H:%M:%S":          "24-hour time",
    "%Y-%m-%d %H:%M:%S": "Full datetime",
}
for fmt, desc in formats.items():
    print(f"  {desc:25} -> {now.strftime(fmt)}")


# ============================================================
# 4. Parsing Strings to Dates (strptime)
# ============================================================
print("\n--- strptime (String -> Date) ---")

date_str = "December 25, 2025"
parsed = datetime.strptime(date_str, "%B %d, %Y")
print(f"  '{date_str}' -> {parsed}")
print(f"  Type: {type(parsed)}")

date_str2 = "2025-03-15 14:30:00"
parsed2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
print(f"  '{date_str2}' -> {parsed2}")


# ============================================================
# 5. timedelta — Date Arithmetic
# ============================================================
print("\n--- timedelta (Date Math) ---")

today = date.today()
one_week = timedelta(weeks=1)
thirty_days = timedelta(days=30)

print(f"  Today:          {today}")
print(f"  In 1 week:      {today + one_week}")
print(f"  30 days ago:    {today - thirty_days}")
print(f"  In 100 days:    {today + timedelta(days=100)}")

# Difference between dates
future = date(2026, 1, 1)
diff = future - today
print(f"  Days until {future}: {diff.days}")

# Time differences
start = datetime(2025, 1, 1, 8, 0, 0)
end = datetime(2025, 1, 1, 17, 30, 0)
work_hours = end - start
print(f"  Work hours: {work_hours}")
print(f"  In seconds: {work_hours.total_seconds()}")


# ============================================================
# 6. Comparing Dates
# ============================================================
print("\n--- Comparing Dates ---")
d1 = date(2025, 6, 15)
d2 = date(2025, 12, 25)
print(f"  {d1} < {d2}: {d1 < d2}")
print(f"  {d1} == {d2}: {d1 == d2}")

# Checking if a date is in the past or future
if date.today() < d2:
    print(f"  {d2} is in the future")


# ============================================================
# 7. Calendar Module
# ============================================================
print("\n--- Calendar ---")
print(f"  Is 2024 a leap year? {calendar.isleap(2024)}")
print(f"  Is 2025 a leap year? {calendar.isleap(2025)}")
print(f"  Days in Feb 2024: {calendar.monthrange(2024, 2)[1]}")
print(f"  Days in Feb 2025: {calendar.monthrange(2025, 2)[1]}")
