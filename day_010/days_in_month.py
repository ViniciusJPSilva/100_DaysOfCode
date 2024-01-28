def check_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month < 1 or month > 12: 
    return
  
  return month_days[month - 1] if month != 2 or not check_leap_year(year) else 29

year = int(input("Enter a year: ")) # Enter a year
month = int(input("Enter a month: ")) # Enter a month
days = days_in_month(year, month)
print(f"\nIn the year {year}, month {month} will have {days} days!\n")