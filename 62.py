# Write a Python program to convert all units of time into seconds.


def seconds(y, mo, w, d, h, m, s):
  yrs = y * (60 * 60 * 24 * 365.25)
  mths = mo * (60 * 60 * 24 * 30)
  wks = w * (60 * 60 * 24 * 7)
  dys = d * (60 * 60 * 24)
  hrs = h * (60 * 60)
  mins = m * (60)
  sec = s 

  result = yrs + mths + wks + dys + hrs + mins + sec 

  return result

print("** Second Converter **")
years = int(input('Enter number of years: '))
months = int(input('Enter number of months: '))
weeks = int(input('Enter number of weeks: '))
days = int(input('Enter number of days: '))
hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
second = int(input('Enter number of seconds: '))

ans = seconds(years, months, weeks, days, hours, minutes, second)

print('Total seconds:', ans)