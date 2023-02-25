def is_leap(year: int):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def days_in_month(year: int, month: int):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 29 if is_leap(year) and month == 2 else month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
