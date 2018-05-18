# Write a Python program to convert seconds to day, hour, minutes and seconds.


def sec_converter(s):
  day_secs = 60 * 60 * 24
  hour_secs = 60 * 60
  min_secs = 60

  days = 0
  hours = 0
  mins = 0
  secs = 0

  mins = s 

  if s > day_secs:
    days = int(s / day_secs)

    s = s - (days * day_secs)

  if s > hour_secs:
    hours = int(s / hour_secs)

    s = s - (hours * hour_secs)

  if s > min_secs:
    mins = int(s / min_secs)

    s = int(s - (mins * min_secs))

  secs = s 

  result = f"{days} days: {hours} hours: {mins} mins: {secs} secs"

  print(result)


sec_converter(500)
sec_converter(5000)

sec_converter(20000)

sec_converter(200000)


